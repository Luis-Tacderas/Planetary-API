# Sample Python Restful API using Flask Blueprint

## Python libraries required
	pip install SQLAlchemy
	pip install Flask
	pip install Flask-SQLAlchemy
	pip install python-dotenv

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

### Get request: http://127.0.0.1:5000/parameters?name=Luis&age=56

{
    "message": "Welcome Luis, you are old enough!"
}

### Get request: http://127.0.0.1:5000/url_variables/Luis/56

{
    "message": "Welcome Luis, you are old enough!"
}