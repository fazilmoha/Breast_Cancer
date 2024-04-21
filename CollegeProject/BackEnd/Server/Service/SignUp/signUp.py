from flask import Flask, request, jsonify
from Service.Utils.users_data import load_users, save_users

def signUp():
    users = load_users()
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users:
        return jsonify({'message': 'Username already exists'}), 400

    users[username] = {'password': password}
    save_users(users)
    return jsonify({'message': 'User created successfully'}), 201