from flask import jsonify, request
from Models.order import Order
from extensions import db

def save_order():
    data = request.get_json()
    new_order = Order(
        customer_id=data['customer_id'],
        product_id=data['product_id'],
        quantity=data['quantity'],
        total_price=data['total_price']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order saved"}), 201

def get_order():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])
