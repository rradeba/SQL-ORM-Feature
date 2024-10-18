from flask import Blueprint, jsonify
from flask_limiter import Limiter
from Controllers.customerController import save_customer, get_customer

customer_blueprint = Blueprint('order', __name__)

@customer_blueprint.route('/customer', methods=['POST'])(save_customer)
@Limiter.limit("5 per minute")  
def create_customer():
    return jsonify({"message": "Customer created"})


@customer_blueprint.route('/customer/<int:customer_id>', methods=['GET'])(get_customer)
@Limiter.limit("10 per minute") 
def get_order(order_id):
    return jsonify({"message": f"Customer {order_id}"})