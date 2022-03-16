from src.utils.external1 import *
from src.utils.external2 import *
from src.database.ipDB import *
from src.app_server import *

from flask import Flask, jsonify, make_response,  request, render_template
app = Flask(__name__)



# Base Flask main app script

# Each method deals with an endpoint and sends back a JSON response or a web page


# Base endpoint -  not much going on here
@app.route('/')
def Home():

    return render_template('templates/index.html')



# GET endpoint - sends a list of all IPs collected from two distinct sources
@app.get('/fullList')
def fullList():

    resp = server_FetchFullList()

    return make_response(jsonify(resp))
    


# POST endpoint - receives an object {'ip': '<ip_value>'} and store in a database
@app.post('/ban_ip')
def banIP():

    data = request.get_json() 
    server_BanIP(data['ip'])

    resp = {'data': len(server_getBlacklist())}
    return make_response(jsonify(resp))



# GET endpoint - sends a new list excluding all registered banned IPs
@app.get('/validList')
def ValidList():

    resp = server_FetchValidList()

    return make_response(jsonify(resp))




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



    