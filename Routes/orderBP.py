from flask import Blueprint, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from Controllers.orderController import save_order, get_order as get_order_data

order_blueprint = Blueprint('order', __name__)
limiter = Limiter(get_remote_address)

@order_blueprint.route('/order', methods=['POST'])
def create_order():
    order_data = request.json
    result = save_order(order_data)
    return jsonify(result)

@order_blueprint.route('/employee/<int:order_id>', methods=['GET'])
@limiter.limit("10 per minute")  # Use the local limiter instance
def get_order_route(order_id):
    result = get_order_data(order_id)
    return jsonify(result)
