import pymssql
from flask import Flask, request, jsonify
from flask_cors import CORS


file = open('config/development.json', 'r')
config = eval(file.read())


app = Flask(__name__)
CORS(app)

connection = pymssql.connect(config['host'], config['user'],
                             config['password'], config['db'])



if __name__ == '__main__':
    app.run(debug=True)
