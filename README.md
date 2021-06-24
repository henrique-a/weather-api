# weather-api

## About
A service that collects data from an Open Weather API and store it as
a JSON data. 

The API was developed in Django with Django REST framework, a powerful framework to build web REST APIs. The data is stored in a SQLite database, a simple and light database.

## Endpoints
- POST /api/requests?id={userid} 
Receives a user defined ID, collect weather data from Open Weather API and store:
    - The user defined ID (needs to be unique for each request)
    - Datetime of request
    - JSON data with:
        - City ID
        - Temperature in Celsius
        - Humidity
   
 - GET /api/weather-data?id={userid}
 
 Receives the user defined ID, returns with the percentage of the POST progress ID (collected cities completed) until the current moment.

## Setup and Run on localhost
1. Build Docker image
```
docker build -t weatherapi:1.0 . --network host
```
2. Run with Compose
```
docker-compose -f docker-compose.yaml up
```
3. Test
- POST http://127.0.0.1:8000/api/requests?id={userid}
- GET http://127.0.0.1:8000/api/weather-data?id={userid}

