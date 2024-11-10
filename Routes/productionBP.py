from flask import Blueprint, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from Controllers.productionController import save_production, get_production

production_blueprint = Blueprint('production', __name__)
limiter = Limiter(key_func=get_remote_address)  # Initialize limiter

@production_blueprint.route('/production', methods=['POST'])
@limiter.limit("5 per minute")  # Apply rate limiting
def create_production():
    production_data = request.json
    result = save_production(production_data)
    return jsonify(result)

@production_blueprint.route('/production/<int:production_id>', methods=['GET'])
@limiter.limit("10 per minute")  # Apply rate limiting
def get_production_route(production_id):
    result = get_production(production_id)
    return jsonify(result)
