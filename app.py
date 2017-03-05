from flask import Flask, request, jsonify, Response
import os
import RESTAPI

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "omg my backend is working"

@app.route('/test-route')
def show_test():
	return "testing!"

@app.route('/post-test', methods=['POST','GET'])
def test_backend():
	return RESTAPI.test(request.get_json())

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    print('RUNNING FLASK APP ON PORT: ' + str(port))
    app.run(host='0.0.0.0',port = port, debug = True)