from flask import Flask, request, jsonify
from Service.Utils.users_data import load_users

def login():
    users = load_users()
    print(request.json)
    username = request.json.get('username')
    password = request.json.get('password')

    if username not in users or users[username]['password'] != password:
        return jsonify({'message': 'Invalid username or password'}), 401

    return jsonify({'message': 'Login successful'}), 200 