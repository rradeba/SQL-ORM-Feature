from flask import Blueprint, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from Controllers.employeeController import save_employee, get_employee

employee_blueprint = Blueprint('employee', __name__)
limiter = Limiter(key_func=get_remote_address) 

@employee_blueprint.route('/employee', methods=['POST'])
@limiter.limit("5 per minute") 
def create_employee():
    employee_data = request.json
    result = save_employee(employee_data)
    return jsonify(result)

@employee_blueprint.route('/employee/<int:employee_id>', methods=['GET'])
@limiter.limit("10 per minute") 
def get_employee_route(employee_id):
    result = get_employee(employee_id)
    return jsonify(result)

