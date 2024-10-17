from flask import Blueprint, jsonify
from flask_limiter import Limiter
from Controllers.orderController import save_order, get_order

order_blueprint = Blueprint('order', __name__)

@order_blueprint.route('/order', methods=['POST'])(save_order)
@Limiter.limit("5 per minute")  
def create_order():
    return jsonify({"message": "Order created"})


@order_blueprint.route('/employee/<int:order_id>', methods=['GET'])(get_order)
@Limiter.limit("10 per minute") 
def get_order(order_id):
    return jsonify({"message": f"Order {order_id}"})
