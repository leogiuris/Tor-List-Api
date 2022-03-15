from utils.external1 import *
from utils.external2 import *
from database.ipDB import *
import app_server

from flask import Flask, jsonify, make_response, render_template, request
app = Flask(__name__)




@app.route('/')
def Home():
    
    mockList = ["index page"]

    return make_response(jsonify(mockList))



@app.get('/fullList')
def fullList():

    resp = app_server.FetchFullList()

    return make_response(jsonify(resp))
    


@app.post('/ban_ip')
def banIP():

    data = request.get_json()
    print(data['ip'])

    app_server.BanIP(data['ip'])

    resp = {'resposta': 'do api'}
    return make_response(jsonify(resp))



@app.get('/validList')
def ValidList():

    resp = app_server.FetchValidList()

    return make_response(jsonify(resp))




if __name__ == '__main__':
    app.run(debug=True)



