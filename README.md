# Tor-List-Api
A RESTful API using Flask that compiles IP addresses from two distict third-party APIs.


## Endpoints

Base URL. Currently returns a placeholder static page.
```bash
(Base) localhost:5000/
```

### 1
This endpoint provides a complete list with all the IPs gathered fetching the sources.
```bash
(GET) /fullList
```
(can be loaded on browser)


### 2
This endpoint receives a Json object in the format {'ip': '<ip_address>'} in a Post request. It allows the user to mark that IP address as 'banned', effectively blacklisting them.
```bash
(POST) /ban_ip
```


### 3
This endpoint returns the same list from endpoint 1 but excludes the IP addresses marked as 'banned'.
```bash
(GET) /validList
```
(can be loaded on browser)


## How to run on a Docker Container:

On the command prompt, go to the same directory as Main.py and run:
```bash
docker build -t flask_docker_test .
```

```bash
docker run -d -p 5000:5000 flask_docker_test
```


You can test the app by running simple scripts such as test.py and test.js (using Node.js) that send Get and Post requests to the server. 

You may want to take them out of the app directory and run them from some place else, like the Desktop path.


