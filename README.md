# flask-proxy

### How to start

Run the following command to build the docker image `flask-proxy` from root directory:
```sh
docker build -t flask-proxy:latest
```

Run the docker container
```sh
 docker run -p 5000:5000 flask-proxy 
```

Then go to http://0.0.0.0:5000 to be able to see what's going out.

