#advanced queries for exercise 2 


from sqlalchemy import func
from Models import employee, product, production, order, customer
from extensions import db

def analyze_employee_performance():
    query = (
        db.session.query(employee.name, func.sum(production.quantity).label("total_quantity"))
        .join(production, production.employee_id == employee.id)
        .group_by(employee.name)
    )
    return query.all()

def identify_top_selling_products():
    query = (
        db.session.query(product.name, func.sum(order.quantity).label("total_quantity_ordered"))
        .join(order, order.product_id == product.id)
        .group_by(product.name)
        .order_by(func.sum(order.quantity).desc())
    )
    return query.all()

def calculate_customer_lifetime_value(value):
    query = (
        db.session.query(customer.name, func.sum(order.total_value).label("total_order_value"))
        .join(order, order.customer_id == customer.id)
        .group_by(customer.name)
        .having(func.sum(order.total_value) >= value)
    )
    return query.all()

def evaluate_production_efficiency(date):
    query = (
        db.session.query(product.name, func.sum(production.quantity).label("total_quantity"))
        .join(production, production.product_id == product.id)
        .filter(production.date == date)
        .group_by(product.name)
    )
    return query.all()
