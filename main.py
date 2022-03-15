from src.utils.external1 import *
from src.utils.external2 import *
from src.database.ipDB import *
from src.app_server import *

from flask import Flask, jsonify, make_response,  request, render_template
app = Flask(__name__)




@app.route('/')
def Home():

    return render_template('templates/index.html')


# GET endpoint - sends a list of all IPs collected from two distinct sources
@app.get('/fullList')
def fullList():

    resp = FetchFullList()

    return make_response(jsonify(resp))
    

# POST endpoint - receives an object {'ip': '<ip_value>'} and store in a database
@app.post('/ban_ip')
def banIP():

    data = request.get_json() 
    BanIP(data['ip'])

    resp = {'resposta': 'do api'}
    return make_response(jsonify(resp))



@app.get('/validList')
def ValidList():

    resp = FetchValidList()

    return make_response(jsonify(resp))




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')