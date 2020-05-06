import pymssql
from flask import Flask, request, jsonify
from flask_cors import CORS


file = open('config/development.json', 'r')
config = eval(file.read())


app = Flask(__name__)
CORS(app)

connection = pymssql.connect(config['host'], config['user'],
                             config['password'], config['db'])


@app.route('/users/create', methods=['POST'])
def createUser():
    userInfo = [request.json['idCard'], request.json['name'],
            request.json['lastname'], request.json['phoneNumber'],
            request.json['email']]
    
    cursor = connection.cursor()

    response = {
        'message': 'Unkown error.',
        'status': 404,
        'data': None
    }

    try:
        cursor.callproc('createUser', userInfo)
        connection.commit()

        response = {
            'message': 'User was created.',
            'status': 400,
            'data': None
        }
    except pymssql.OperationalError as e:
        print(e)
    except pymssql.DatabaseError:
        response = {
            'message': 'ID Card already exists.',
            'status': 400,
            'data': None
        }

    cursor.close()

    return jsonify(response)

@app.route('/users/<_id>', methods=['DELETE'])
def deleteUser(_id):
    cursor = connection.cursor()
    cursor.callproc('deleteUser', [_id])
    cursor.nextset()

    response = {}

    try:
        connection.commit()

        response = {
            'message': 'User was deleted.',
            'status': 400,
            'data': None
        }
    except pymssql.OperationalError:
        response = {
            'message': 'User not found.',
            'status': 404,
            'data': None
        }

    cursor.close()

    return jsonify(response)

@app.route('/users/<_id>', methods=['GET'])
def getUserById(_id):
    cursor = connection.cursor()
    cursor.callproc('getUserByID', [_id])
    cursor.nextset()

    response = {}

    try:
        result = cursor.fetchone()
        connection.commit()
        
        user = {
            '_id': result[1],
            'idCard': result[0],
            'email': result[5],
            'lastname': result[3],
            'name': result[3],
            'phoneNumber': result[4]
        }

        response = {
            'message': 'Returing user.',
            'status': 400,
            'data': user
        }
    except pymssql.OperationalError:
        response = {
            'message': 'User not found.',
            'status': 404,
            'data': None
        }

    cursor.close()

    return jsonify(response)

@app.route('/users', methods=['GET'])
def getUsers():
    cursor = connection.cursor()
    cursor.callproc('getUsers')
    cursor.nextset()
    users = []

    try:
        results = cursor.fetchall()
        connection.commit()
        
        users = []
        for user in results:
            users.append({
                '_id': user[1],
                'idCard': user[0],
                'email': user[5],
                'lastname': user[3],
                'name': user[3],
                'phoneNumber': user[4]
            })
    except pymssql.OperationalError:
        pass

    cursor.close()

    return jsonify({
        'message': 'Returing all users.',
        'status': 400,
        'data': users
    })

@app.route('/users/<_id>', methods=['PUT'])
def updateUser(_id):
    userInfo = [_id, request.json['idCard'], request.json['name'],
            request.json['lastname'], request.json['phoneNumber'],
            request.json['email']]
    
    cursor = connection.cursor()

    response = {
        'message': 'Unkown error.',
        'status': 404,
        'data': None
    }

    try:
        cursor.callproc('updateUser', userInfo)
        connection.commit()

        response = {
            'message': 'User was updated.',
            'status': 400,
            'data': None
        }
    except pymssql.OperationalError as e:
        response = {
            'message': 'ID Card not found.',
            'status': 400,
            'data': None
        }

    cursor.close()

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
