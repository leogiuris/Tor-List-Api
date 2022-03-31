# Tor-List-Api
A RESTful API using Flask that compiles TOR IP addresses from two distict third-party APIs.


## Endpoints


### Base URL - localhost:5000/
Base URL. Currently returns a placeholder static page.



### 1 -  GET /fullList
This endpoint provides a complete list with all the IPs gathered fetching the sources.
(can be loaded on browser)


### 2 - POST /ban_ip
This endpoint receives a Json object in the format {'ip': '<ip_address>'} in a Post request. It allows the user to mark that IP address as 'banned', effectively blacklisting them.


### 3 - GET /validList
This endpoint returns the same list from endpoint 1 but excludes the IP addresses marked as 'banned'.
(can be loaded on browser)


## How to run on a Docker Container:

On the command prompt, go to the same directory as Main.py and run:
```bash
docker build -t flask_docker_test .
```

```bash
docker run -d -p 5000:5000 flask_docker_test
```


Once the server is running, via Docker or locally, you have two ways to interact
with the API: through the server's provided view (type 'http://localhost:5000' on your browser) or you can access through your own frontend app.

### Through the server's provided View
You can interact on your browser by typing 'http://localhost:5000' on the address bar. This is because the API returns an HTML view when the request is not Application/JSON content-type.

### Through JSON requests
To request JSON data for your own project, you can send http 'get' and 'post' requests. To do so you must add the following headers:

```bash
{'Content-Type': 'application/json'}
```
```bash
{'Access-Control-Allow-Origin': '*'}
```

To send a 'post' request, the body must follow the format 
{'ip_address': <'address string'>}

i.e: {'ip_address': '0.0.0.0'}