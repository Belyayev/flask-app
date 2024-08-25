#!/bin/bash

# Stop and remove the existing container
docker stop flask-app
docker rm flask-app

# Build the updated image
docker build -t flask-app .

# Run the updated container
docker run -p 5000:5000 --name flask-app --link sqlserver:sqlserver -d flask-app
