from flask import Blueprint, jsonify
from flask_limiter import Limiter
from Controllers.productController import save_product, get_product

product_blueprint = Blueprint('product', __name__)

@product_blueprint.route('/product', methods=['POST'])(save_product)
@Limiter.limit("5 per minute")  
def create_product():
    return jsonify({"message": "Product created"})


@product_blueprint.route('/product/<int:product_id>', methods=['GET'])(get_product)
@Limiter.limit("10 per minute") 
def get_product(product_id):
    return jsonify({"message": f"Product {product_id}"})
