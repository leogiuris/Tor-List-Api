from importlib import import_module
from src.database.ipDB import *
from src.app_server import *

from flask import Flask, jsonify, url_for, make_response, redirect, request, render_template

app = Flask(__name__, template_folder='templates')


# Base Flask main app script

# Each method deals with an endpoint and sends back a JSON response or a web page





# Base endpoint -  not much going on here
@app.route('/')
def Index():
    return render_template('index.html')






# GET endpoint - sends a list of all IPs collected from two distinct sources
@app.get('/fullList')
def FullList(all='False'):
    print(all)
    resp = server_FetchFullList()
    if request.is_json:
        resp = make_response(jsonify(resp))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        if all == True:
            size = len(resp)
        else:
            size = int(request.args.get('size',default='100'))
        bans = {}
        for ip in server_getBlacklist():
            try:
                bans[ip] = "banned"
            except:
                print(ip + ": Ip not in list")
        return render_template('fullList.html', total = len(resp), len = len(resp[0:size]), ips = resp, bans = bans)

    



# POST endpoint - receives an object {'ip_address': '<ip_value>'} and store in a database
@app.post('/ban_ip')
def BanIP():

    if request.is_json:
        req = request.get_json()
        server_BanIP(req['ip_address'])
        resp = make_response(jsonify(''))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        req = request.form.get('ip_address')
        server_BanIP(req)
        return redirect(url_for('FullList'))





# GET endpoint - sends a new list excluding all registered banned IPs
@app.get('/validList')
def ValidList():
    resp = server_FetchValidList()
    if request.is_json:
        resp = make_response(jsonify(resp))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        size = int(request.args.get('size',default='100'))
        index = int(request.args.get('index',default='0'))
        return render_template('validList.html', total = len(resp), len = len(resp[index:index+size]), ips = resp)





@app.get('/bannedList')
def BannedList():
    resp = server_getBlacklist()
    if request.is_json:
        resp = make_response(jsonify(resp))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        size = int(request.args.get('size',default='100'))
        index = int(request.args.get('index',default='0'))
        return render_template('bannedList.html', len = len(resp), ips = resp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



    