from flask import Blueprint, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from Controllers.customerController import save_customer, get_customer

customer_blueprint = Blueprint('customer', __name__)
limiter = Limiter(key_func=get_remote_address) 

@customer_blueprint.route('/customer', methods=['POST'])
@limiter.limit("5 per minute")  
def create_customer():
    customer_data = request.json
    result = save_customer(customer_data)
    return jsonify(result)

@customer_blueprint.route('/customer/<int:customer_id>', methods=['GET'])
@limiter.limit("10 per minute") 
def get_customer_route(customer_id):
    result = get_customer(customer_id)
    return jsonify(result)

