from flask import Flask
from extensions import db, ma, migrate 
from Routes.orderBP import order_blueprint
from Routes.customerBP import customer_blueprint
from Routes.productBP import product_blueprint
from Routes.productionBP import production_blueprint
from Routes.employeeBP import employee_blueprint
from Routes.advanced_queries_BP import advanced_queries_blueprint 
from limiter import limiter
import os 
from dotenv import load_dotenv 

load_dotenv()

def create_app(config_name='development'):
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

   
    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)

 
    app.register_blueprint(order_blueprint, url_prefix='/api/orders')
    app.register_blueprint(customer_blueprint, url_prefix='/api/customers')
    app.register_blueprint(employee_blueprint, url_prefix='/api/employees')
    app.register_blueprint(product_blueprint, url_prefix='/api/products')
    app.register_blueprint(production_blueprint, url_prefix='/api/productions')
    app.register_blueprint(advanced_queries_blueprint, url_prefix='/api/advanced_queries')

    return app


if __name__ == '__main__':

    app = create_app('DevelopmentConfig')  
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
