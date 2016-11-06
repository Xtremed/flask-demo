# -*- coding: utf-8 -*-
"""
    flaskDemo
    ~~~~~~~~~

    This is a demo using Python Flask, used only for learning purposes.

    :license: IST.
"""

#:Requirements
import requests
from flask import Flask, render_template, request, jsonify, json, Response

app = Flask(__name__)

#Renders Home Template
@app.route('/')
def index():
    return render_template('index.html')

#Renders Update Template
@app.route('/update')
def update():
    return render_template('update.html')

#: Error Handler Function 404
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

#: Error Handler Function 409
@app.errorhandler(409)
def conflict(error=None):
    message = {
            'status': 409,
            'message': 'Conflict: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 409
    return resp

#: getUsers Endpoint
@app.route("/users", methods = ['GET'])
def api_users():
    """In here I decided to use the Response library to show two
    different approaches on how to send responses, compared with
    just returning the json object as seen in api_user()
    """

    r = requests.get("https://jsonplaceholder.typicode.com/users");
    js = json.dumps(r.text)
    resp = Response(js, status=200, mimetype='application/json');
    return resp

#: getUsersbyID Endpoint
@app.route('/users/<userid>', methods = ['GET'])
def api_user(userid):
    r = requests.get("https://jsonplaceholder.typicode.com/users/"+userid);
    if(r):
        return jsonify(result=r.text)
    else:
        return not_found()

#: updateUsers Endpoint
@app.route('/users/<userid>', methods = ['PATCH','PUT'])
def api_mod_user(userid):
    if (request.form):
        r = requests.patch("https://jsonplaceholder.typicode.com/users/"+userid, request.form);
        return jsonify(result=r.text)
    else:
        conflict()

if __name__ == '__main__':
    app.run(debug=True)
