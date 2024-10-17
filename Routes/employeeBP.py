from flask import Blueprint, jsonify
from flask_limiter import Limiter
from Controllers.employeeController import save_employee, get_employee

employee_blueprint = Blueprint('employee', __name__)

@employee_blueprint.route('/employee', methods=['POST'])(save_employee)
@Limiter.limit("5 per minute")  
def create_employee():
    return jsonify({"message": "Employee created"})


@employee_blueprint.route('/employee/<int:employee_id>', methods=['GET'])(get_employee)
@Limiter.limit("10 per minute") 
def get_employee(employee_id):
    return jsonify({"message": f"Employee {employee_id}"})




