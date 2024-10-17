from flask import jsonify, request
from Models.customer import Customer
from extensions import db

def save_customer():
    data = request.get_json()
    new_customer = Customer(
        customer_id=data['customer_id'],
        customer_name=data['customer_name'],
        customer_email =data['customer_email'],
        customer_phone=data['customer_phone']
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "Customer saved"}), 201

def get_customer():
    customer = Customer.query.all()
    return jsonify([customer.to_dict() for customers in customer])