import pymssql
from flask import Flask, request, jsonify
from flask_cors import CORS


file = open('config/development.json', 'r')
config = eval(file.read())


app = Flask(__name__)
CORS(app)

connection = pymssql.connect(config['host'], config['user'],
                             config['password'], config['db'])

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
    connection.close()

    return jsonify({
        'message': 'Returing all users.',
        'status': 400,
        'data': users
    })

if __name__ == '__main__':
    app.run(debug=True)
