from flask import Blueprint, jsonify, request
from database.model import User, Planet, planets_schema, users_schema

route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/')
def index():
    return "Routed to Main of App"


@route_blueprint.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the Route Blueprint!'), 200


@route_blueprint.route('/planets', methods=['GET'])
def planets():
    planets_list = Planet.query.all()
    return jsonify(planets_schema.dump(planets_list))


@route_blueprint.route('/users', methods=['GET'])
def users():
    users_list = User.query.all()
    return jsonify(users_schema.dump(users_list))


@route_blueprint.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message='Sorry ' + name + ', you are not old enough.'), 401
    else:
        return jsonify(message='Welcome ' + name + ', you are old enough!')


@route_blueprint.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
   if age < 18:
        return jsonify(message='Sorry ' + name + ', you are not old enough.'), 401
   else:
        return jsonify(message='Welcome ' + name + ', you are old enough!')
 

