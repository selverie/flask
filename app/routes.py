# app/routes.py
from app import app
from app.controller import UserController
from flask import request

@app.route('/users', methods=['GET'])
def get_users():
    return UserController.index()

@app.route('/users', methods=['POST'])
def create_user():
    return UserController.store()

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)
