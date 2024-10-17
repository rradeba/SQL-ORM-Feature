from flask import jsonify, request
from Models.production import Production
from extensions import db

def save_production():
    data = request.get_json()
    new_production = Production(
        production_id=data['production_id'],
        production_quantity=data['production_quantity'],
        production_date=data['production_date']
    )
    db.session.add(new_production)
    db.session.commit()
    return jsonify({"message": "Production saved"}), 201

def get_production():
    productions = Production.query.all()
    return jsonify([production.to_dict() for production in productions])