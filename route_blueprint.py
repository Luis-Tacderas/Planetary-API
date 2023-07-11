from flask import Blueprint, jsonify

route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/')
def index():
    return "This is an example app"


@route_blueprint.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the Route Blueprint!'), 200
