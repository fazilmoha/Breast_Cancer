from flask import Flask, request, jsonify
import requests

def getHospitals():
    city = request.args.get('city')
    
    # Use OpenStreetMap Nominatim API to get the latitude and longitude of the city
    nominatim_url = f'https://nominatim.openstreetmap.org/search?city={city}&format=json'
    nominatim_response = requests.get(nominatim_url)
    if nominatim_response.status_code == 200:
        nominatim_data = nominatim_response.json()
        if nominatim_data:
            lat = nominatim_data[0]['lat']
            lon = nominatim_data[0]['lon']
        else:
            return jsonify({'error': 'City not found'}), 404
    else:
        return jsonify({'error': 'Failed to fetch city details'}), 500
    
    # Use OpenStreetMap Overpass API to search for hospitals near the latitude and longitude
    overpass_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node(around:5000,{lat},{lon})["amenity"="hospital"];out;'
    overpass_response = requests.get(overpass_url)
    if overpass_response.status_code == 200:
        overpass_data = overpass_response.json()
        hospitals = [node['tags']['name'] for node in overpass_data['elements']]
        return jsonify({'hospitals': hospitals})
    else:
        return jsonify({'error': 'Failed to fetch hospitals'}), 500
