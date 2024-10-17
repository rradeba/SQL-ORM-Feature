from flask import Blueprint, jsonify
from flask_limiter import Limiter
from Controllers.productionController import save_production, get_production

production_blueprint = Blueprint('production', __name__)

@production_blueprint.route('/production', methods=['POST'])(save_production)
@Limiter.limit("5 per minute")  
def create_production():
    return jsonify({"message": "Production created"})


@production_blueprint.route('/production/<int:production_id>', methods=['GET'])(get_production)
@Limiter.limit("10 per minute") 
def get_production(production_id):
    return jsonify({"message": f"Production {production_id}"})
