from flask import Blueprint, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from Controllers.productController import save_product, get_product

product_blueprint = Blueprint('product', __name__)
limiter = Limiter(key_func=get_remote_address)  # Ensure limiter is properly initialized

@product_blueprint.route('/product', methods=['POST'])
@limiter.limit("5 per minute")  # Apply rate limiting
def create_product():
    product_data = request.json
    result = save_product(product_data)
    return jsonify(result)

@product_blueprint.route('/product/<int:product_id>', methods=['GET'])
@limiter.limit("10 per minute")  # Apply rate limiting
def get_product_route(product_id):
    result = get_product(product_id)
    return jsonify(result)
