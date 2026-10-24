# superkart-prediction-app
SuperKart Price Prediction - Flask API Backend + Streamlit Frontend (Dockerized)
<br>

## Deployment on Github Spaces

1. **Create docker network to connect frontend and backend containers**
```sh
docker network create superkart-app-network
```
<br>

2. **Build backend image and run the container on the network.**<br>
```sh
cd backend
docker build -t superkart-backend .
docker run -d --name backend --network superkart-app-network -p 7860:7860 superkart-backend
```
<br>

3. **Build frontend image and run the container on the network.**<br>
```sh
cd ../frontend
docker build -t superkart-frontend .
docker run -d --name frontend --network superkart-app-network -p 8501:8501 -e BACKEND_URL="http://172.18.0.1:7860" superkart-frontend
```
*BACKEND_URL="http://172.18.0.1:7860" is added to use the Host Network when http://backend:7860 does not work*
