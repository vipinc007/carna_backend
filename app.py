from flask import Flask, jsonify, request
from flask_cors import CORS
from data_manager import data_manager
from object_manager import object_manager

from DataManager.userManager import user_manager

app = Flask(__name__)
CORS(app)

listofObjects = 'ListOfObjects'
objm = object_manager(listofObjects)
objm.object_reset()

@app.route('/object/create', methods=['GET'])
def object_create():
    res = objm.object_create()
    return jsonify(result=res)

@app.route('/user/save', methods=['POST'])
@app.route('/user/save/<id>', methods=['POST'])
def user_create(id=None):
    user = request.json
    obju = user_manager()
    if id is None:
        res = obju.create(user)
    else:
        res = obju.edit(id,user)
    return jsonify(res)

@app.route('/user/list', methods=['GET'])
@app.route('/user/list/<id>', methods=['GET'])
def user_list(id=None):
    obju = user_manager()
    if id is None:
        res = obju.list()
    else:
        res = obju.get(id)
    return jsonify(result=res)

@app.route('/user/reset', methods=['GET'])
def user_reset():
    obju = user_manager()
    res = obju.reset()
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

