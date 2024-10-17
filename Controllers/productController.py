from flask import jsonify, request
from Models.product import Product 
from extensions import db

def save_product():
    data = request.get_json()
    new_product = Product(
        customer_id=data['product_id'],
        product_name=data['product_name'],
        product_price=data['product_price']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Prouct saved"}), 201

def get_product():
    products = Product.query.all()
    return jsonify(product.to_dict() for product in products)