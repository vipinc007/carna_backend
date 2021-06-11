from flask import Flask, jsonify
from flask_cors import CORS
from data_manager import data_manager
from object_manager import object_manager

app = Flask(__name__)
CORS(app)

listofObjects = 'ListOfObjects'
objm = object_manager(listofObjects)
objm.object_reset()

@app.route('/object/create', methods=['GET'])
def object_create():
    res = objm.object_create()
    return jsonify(result=res)

@app.route('/object/reset', methods=['GET'])
def object_reset():
    res = objm.object_reset()
    return jsonify(result=res)

@app.route('/object/get', methods=['GET'])
def object_get():
    res = objm.object_get()
    return jsonify(result=res)

@app.route('/object/list', methods=['GET'])
def object_list():
    res = objm.object_list()
    return jsonify(result=res)

@app.route('/object/free/<num>', methods=['GET'])
def object_free(num):
    res = objm.object_free(num)
    return jsonify(result=res)

if __name__ == '__main__':
    app.run()

