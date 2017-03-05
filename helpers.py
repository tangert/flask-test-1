from flask import jsonify

def response(data={}):
    response = jsonify(data)
    response.status_code = 200
    return response
