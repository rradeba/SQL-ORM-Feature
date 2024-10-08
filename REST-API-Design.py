# Libraries 
from flask import Flask, jsonify, request  
from flask_sqlalchemy import SQLAlchemy  
from flask_limiter import Limiter  
from flask_limiter.util import get_remote_address  


dataBase = SQLAlchemy()  
limiter = Limiter(
    key_func=get_remote_address,  
    default_limits=["100 per hour", "20 per minute"] 
)

# Define databases
class Employee(dataBase.Model):
    __tablename__ = 'employees'  
    id = dataBase.Column(dataBase.Integer, primary_key=True)  
    name = dataBase.Column(dataBase.String(100), nullable=False)  
    position = dataBase.Column(dataBase.String(100), nullable=False)  

class Product(dataBase.Model):
    __tablename__ = 'products'  
    id = dataBase.Column(dataBase.Integer, primary_key=True) 
    name = dataBase.Column(dataBase.String(100), nullable=False)  
    price = dataBase.Column(dataBase.Float, nullable=False) 

class Order(dataBase.Model):
    __tablename__ = 'orders'  
    id = dataBase.Column(dataBase.Integer, primary_key=True)  
    customer_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('customers.id'), nullable=False)  
    product_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('products.id'), nullable=False)  
    quantity = dataBase.Column(dataBase.Integer, nullable=False) 
    total_price = dataBase.Column(dataBase.Float, nullable=False)  

class Customer(dataBase.Model):
    __tablename__ = 'customers'  
    id = dataBase.Column(dataBase.Integer, primary_key=True)  
    name = dataBase.Column(dataBase.String(100), nullable=False)  
    email = dataBase.Column(dataBase.String(100), nullable=False)  
    phone = dataBase.Column(dataBase.String(20), nullable=False) 

class Production(dataBase.Model):
    __tablename__ = 'production'  
    id = dataBase.Column(dataBase.Integer, primary_key=True)  
    product_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('products.id'), nullable=False)  
    quantity_produced = dataBase.Column(dataBase.Integer, nullable=False) 
    date_produced = dataBase.Column(dataBase.Date, nullable=False) 

# Flask application
app = Flask(__name__) 


employees_bp = app.route('/employees', methods=['GET', 'POST'])  
products_bp = app.route('/products', methods=['GET', 'POST']) 
orders_bp = app.route('/orders', methods=['GET', 'POST'])  
customers_bp = app.route('/customers', methods=['GET', 'POST'])  
production_bp = app.route('/production', methods=['GET', 'POST']) 


@limiter.limit("10 per minute")  
@limiter.limit("5 per minute")   
@app.route('/employees', methods=['GET'])  
def get_employees():
   
    employees = Employee.query.all() 
    return jsonify([{'id': emp.id, 'name': emp.name, 'position': emp.position} for emp in employees])  

@app.route('/employees', methods=['POST'])  
def add_employee():
    data = request.get_json()  
    new_employee = Employee(name=data['name'], position=data['position'])  
    dataBase.session.add(new_employee)  
    dataBase.session.commit()  
    return jsonify({'message': 'Employee added'}), 201  


@limiter.limit("10 per minute") 
@app.route('/products', methods=['GET']) 
def get_products():
    """Fetch all products from the database."""
    products = Product.query.all()  
    return jsonify([{'id': prod.id, 'name': prod.name, 'price': prod.price} for prod in products]) 

@app.route('/products', methods=['POST'])  
def add_product():
    data = request.get_json()  
    new_product = Product(name=data['name'], price=data['price'])  
    dataBase.session.add(new_product) 
    dataBase.session.commit()  
    return jsonify({'message': 'Product added'}), 201  


@limiter.limit("10 per minute") 
@app.route('/orders', methods=['GET'])  
def get_orders():

    orders = Order.query.all() 
    return jsonify([{'id': ord.id, 'customer_id': ord.customer_id, 'product_id': ord.product_id, 'quantity': ord.quantity, 'total_price': ord.total_price} for ord in orders])  # Return list of orders as JSON

@app.route('/orders', methods=['POST'])  
def add_order():
    data = request.get_json()  
    new_order = Order(customer_id=data['customer_id'], product_id=data['product_id'], quantity=data['quantity'], total_price=data['total_price'])  # Create new order instance
    dataBase.session.add(new_order)  
    dataBase.session.commit() 
    return jsonify({'message': 'Order added'}), 201 


@limiter.limit("10 per minute")  
@app.route('/customers', methods=['GET']) 
def get_customers():
    customers = Customer.query.all()  
    return jsonify([{'id': cust.id, 'name': cust.name, 'email': cust.email, 'phone': cust.phone} for cust in customers])  # Return list of customers as JSON

@app.route('/customers', methods=['POST'])  
def add_customer():
    data = request.get_json() 
    new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone']) 
    dataBase.session.add(new_customer)  
    dataBase.session.commit() 
    return jsonify({'message': 'Customer added'}), 201 


@limiter.limit("10 per minute")  
@app.route('/production', methods=['GET']) 
def get_production():
    production = Production.query.all() 
    return jsonify([{'id': prod.id, 'product_id': prod.product_id, 'quantity_produced': prod.quantity_produced, 'date_produced': prod.date_produced.isoformat()} for prod in production]) 

@app.route('/production', methods=['POST'])  
def add_production():
    data = request.get_json() 
    new_production = Production(product_id=data['product_id'], quantity_produced=data['quantity_produced'], date_produced=data['date_produced'])  
    dataBase.session.add(new_production)  
    dataBase.session.commit()  
