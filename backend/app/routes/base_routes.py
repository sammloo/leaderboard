from flask import Blueprint, jsonify

base_routes = Blueprint('base_routes', __name__)

@base_routes.route('health')
def index():
    return "The server is healthy"



