from utils.external1 import *
from utils.external2 import *
from database.ipDB import *
import app_server

from flask import Flask, jsonify, make_response,  request, render_template
app = Flask(__name__)




@app.route('/')
def Home():
    
    mockList = ["index page"]

    return render_template('index.html')


# GET endpoint - sends a list of all IPs collected from two distinct sources
@app.get('/fullList')
def fullList():

    resp = app_server.FetchFullList()

    return make_response(jsonify(resp))
    

# POST endpoint - receives an object {'ip': '<ip_value>'} and store in a database
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
    app.run(host='0.0.0.0')



