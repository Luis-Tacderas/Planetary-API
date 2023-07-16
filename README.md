# About this project
## Summary
Backend Python restful API using Flask Blueprint and SQLite based on Linkedin tutorial.

## Challenges
None

## Conclusions
It is easy to build backend APIs using python.

## Cool Techniques
Flask Blueprints

## What else I might have done 
1. Use MySQL/Postgres for relational db and MongoDB for no SQl db.
2. Complete all CRUD operation endpoints.
3. Add an external web service call to get more planetary details.

## Python libraries required
	pip install SQLAlchemy
	pip install Flask
	pip install Flask-SQLAlchemy
	pip install python-dotenv
	pip install flask-marshmallow

## Generate requirements.txt
    pip install pipreqs # if not yet installed
    pipreqs 

## To run app
	python app.py

## To test app

### Get request: http://127.0.0.1:5000/

Response: Hello World!

### Get request: http://127.0.0.1:5000/super_simple

{
    "message": "Hello from the Planetary API."
}

### Get request: http://127.0.0.1:5000/api

Response: Routed to Route Blueprint Main

### Get request: http://127.0.0.1:5000/api/super_simple

{
    "message": "Hello from the Route Blueprint API!"
}

### Get request: http://127.0.0.1:5000/api/parameters?name=Luis&age=56

{
    "message": "Welcome Luis, you are old enough!"
}

### Get request: http://127.0.0.1:5000/api/url_variables/Luis/56

{
    "message": "Welcome Luis, you are old enough!"
}

### Get request: http://127.0.0.1:5000/api/planets

[
    {
        "distance": 35980000.0,
        "home_star": "Sol",
        "mass": 3.258e+23,
        "planet_id": 1,
        "planet_name": "Mercury",
        "planet_type": "Class D",
        "radius": 1516.0
    },
    {
        "distance": 67240000.0,
        "home_star": "Sol",
        "mass": 4.867e+24,
        "planet_id": 2,
        "planet_name": "Venus",
        "planet_type": "Class K",
        "radius": 3760.0
    },
    {
        "distance": 92960000.0,
        "home_star": "Sol",
        "mass": 5.972e+24,
        "planet_id": 3,
        "planet_name": "Earth",
        "planet_type": "Class M",
        "radius": 3959.0
    }
]
