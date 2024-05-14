#!.venv/bin/python
"""CRUD API.
"""
import json

from typing import Any, Dict, List, Tuple

import pymssql

from flask import Flask, jsonify, request, Response
from flask_cors import CORS



config: Dict[str, Any]

# Read DB configurations
with open('config/development.json', 'r', encoding='utf-8') as file:
    config = json.loads(file.read())

app: Flask = Flask(__name__)
CORS(app)

connection: pymssql.Connection = pymssql.connect(**config)


@app.route('/users/create', methods=['POST'])
def create_user() -> Response:
    """POST method to create a new user in DB.
    Requires:
        idCard (int) - Identifier number.
        name (str) - First name.
        lastname (str) - Last name.
        phoneNumber (str) - Phone number with country code.
        email (str) - Email address.

    Returns:
        Response: DB response
    """
    # Build user info
    user_info = [
        request.json['idCard'],
        request.json['name'],
        request.json['lastname'],
        request.json['phoneNumber'],
        request.json['email'],
    ]

    cursor: pymssql.Cursor = connection.cursor()

    # Default response
    response: Dict[str, Any] = {
        'message': 'Unkown error.',
        'status': 404,
        'data': None
    }

    try:
        # Call stored procedure to create user
        cursor.callproc('create_user', user_info)
        connection.commit()

        # Successfully created user
        response = {
            'message': 'User was created.',
            'status': 400,
            'data': None
        }
    except pymssql.OperationalError as e:
        print(e)
    except pymssql.DatabaseError:
        # User already exists
        response = {
            'message': 'ID card already exists.',
            'status': 400,
            'data': None
        }

    cursor.close()

    return jsonify(response)

@app.route('/users/<_id>', methods=['DELETE'])
def delete_user(_id: int) -> Response:
    """DELETE method to remove an user from DB.

    Args:
        _id (int): user ID.

    Returns:
        Response: DB response.
    """
    cursor: pymssql.Cursor = connection.cursor()

    # Call store procedure to delete the user by ID
    cursor.callproc('deleteUser', [_id])
    cursor.nextset()

    # Default response
    response: Dict[str, Any] = {}

    try:
        connection.commit()

        # User deleted successfully
        response = {
            'message': 'User was deleted.',
            'status': 400,
            'data': None
        }
    except pymssql.OperationalError:
        # No user with this ID
        response = {
            'message': 'User not found.',
            'status': 404,
            'data': None
        }

    cursor.close()

    return jsonify(response)

@app.route('/users/<_id>', methods=['GET'])
def get_user_by_id(_id: int) -> Response:
    """GET method to retrieve user data by ID from DB.

    Args:
        _id (int): user ID.

    Requires:
        idCard (int) - New identifier number.
        name (str) - New first name.
        lastname (str) - New last name.
        phoneNumber (str) - New phone number with country code.
        email (str) - New email address.

    Returns:
        Response: DB response with the user data.
    """
    cursor: pymssql.Cursor = connection.cursor()

    # Call stored procedure to get data from user
    cursor.callproc('getUserByID', [_id])
    cursor.nextset()

    # Default response
    response: Dict[str, Any] = {}

    try:
        result: Tuple[Any] = cursor.fetchone()
        connection.commit()

        # Prepare response with user data
        response = {
            'message': 'Returing user.',
            'status': 400,
            'data': {
                '_id': result[1],
                'idCard': result[0],
                'email': result[5],
                'lastname': result[3],
                'name': result[3],
                'phoneNumber': result[4]
            }
        }
    except pymssql.OperationalError:
        # User id not found
        response = {
            'message': 'User not found.',
            'status': 404,
            'data': None
        }

    cursor.close()

    return jsonify(response)

@app.route('/users', methods=['GET'])
def get_users() -> Response:
    """GET method to retrieve all the user in DB.

    Returns:
        Response: DB response.
    """
    # Call store procedure to get all users in DB
    cursor: pymssql.Cursor = connection.cursor()
    cursor.callproc('getUsers')
    cursor.nextset()

    # Default response
    response: Dict[str, Any] = {}

    try:
        # Get all users
        results: List[Tuple[Any]] = cursor.fetchall()
        connection.commit()

        users = []

        # Parse user data
        for user in results:
            users.append({
                '_id': user[1],
                'idCard': user[0],
                'email': user[5],
                'lastname': user[3],
                'name': user[3],
                'phoneNumber': user[4]
            })

        response = {
            'message': 'Returing all users.',
            'status': 400,
            'data': users
        }
    except pymssql.OperationalError:
        response = {
            'message': 'No user found.',
            'status': 404,
            'data': []
        }

    cursor.close()

    return jsonify(response)

@app.route('/users/<_id>', methods=['PUT'])
def update_user(_id: int) -> Response:
    """PUT methods to update an user by ID.

    Args:
        _id (int): user ID.

    Returns:
        Response: DB response.
    """
    user_info = [
        _id,
        request.json['idCard'],
        request.json['name'],
        request.json['lastname'],
        request.json['phoneNumber'],
        request.json['email']
    ]

    cursor: pymssql.Cursor = connection.cursor()

    response: Dict[str, Any] = {
        'message': 'Unkown error.',
        'status': 404,
        'data': None
    }

    try:
        cursor.callproc('updateUser', user_info)
        connection.commit()

        response = {
            'message': 'User was updated.',
            'status': 400,
            'data': None
        }
    except pymssql.OperationalError as e:
        print(e)

        response = {
            'message': 'ID Card not found.',
            'status': 400,
            'data': None
        }

    cursor.close()

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
