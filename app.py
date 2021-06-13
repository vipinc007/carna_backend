from flask import Flask, jsonify, request
from flask_cors import CORS
from DataManager.userManager import user_manager

app = Flask(__name__)
CORS(app)


@app.route('/user/save/<id>', methods=['POST'])
def user_create(id):
    user = request.json
    obju = user_manager()
    if int(id) ==0:
        res = obju.create(user)
    else:
        res = obju.edit(id,user)
    return jsonify(res)

@app.route('/user/delete/<id>', methods=['GET'])
def user_delete(id):
    obju = user_manager()
    res = obju.delete(id)
    return jsonify(res)

@app.route('/user/list', methods=['GET'])
@app.route('/user/list/<id>', methods=['GET'])
def user_list(id=None):
    obju = user_manager()
    if id is None:
        res = obju.list()
    else:
        res = obju.get(id)
    return jsonify(res)

@app.route('/user/reset', methods=['GET'])
def user_reset():
    obju = user_manager()
    res = obju.reset()
    return jsonify(result=res)

if __name__ == '__main__':
    app.run()

