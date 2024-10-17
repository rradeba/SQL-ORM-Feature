from flask import jsonify, request
from Models.employee import Employee
from extensions import db

def save_employee():
    data = request.get_json()
    new_employee = Employee(
        employee_id=data['employee_id'],
        employee_name =data['employee_name'],
        employee_position=data['employee_position']
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": "Employee saved"}), 201

def get_employee():
    employees = Employee.query.all()
    return jsonify([employee.to_dict() for employee in employees])