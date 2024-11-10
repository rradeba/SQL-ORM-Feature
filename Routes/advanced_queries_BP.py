from flask import Blueprint, jsonify
from flask_limiter import Limiter
from flask import Flask, jsonify, request

from advanced_queries import analyze_employee_performance, identify_top_selling_products, calculate_customer_lifetime_value, evaluate_production_efficiency



advanced_queries_blueprint = Blueprint('advanced_queries', __name__)



@advanced_queries_blueprint.route('/employee_performance', methods=['GET'])
def get_employee_performance():
    results = analyze_employee_performance()
    return jsonify([{"name": emp.name, "total_quantity": emp.total_quantity} for emp in results])

@advanced_queries_blueprint.route('/top_selling_products', methods=['GET'])
def get_top_selling_products():
    results = identify_top_selling_products()
    return jsonify([{"product_name": prod.name, "total_quantity_ordered": prod.total_quantity_ordered} for prod in results])

@advanced_queries_blueprint.route('/customer_lifetime_value', methods=['GET'])
def get_customer_lifetime_value():
    threshold_value = request.args.get("threshold", default=500, type=int)
    results = calculate_customer_lifetime_value(threshold_value)
    return jsonify([{"customer_name": cust.name, "total_order_value": cust.total_order_value} for cust in results])

@advanced_queries_blueprint.route('/production_efficiency', methods=['GET'])
def get_production_efficiency():
    specific_date = request.args.get("date", type=str)
    if specific_date is None:
        return jsonify({"error": "Date parameter is required"}), 400
    results = evaluate_production_efficiency(specific_date)
    return jsonify([{"product_name": prod.name, "total_quantity": prod.total_quantity} for prod in results])

