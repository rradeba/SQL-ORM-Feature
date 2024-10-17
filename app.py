from flask import Flask
from extensions import db, ma
from Routes.orderBP import order_blueprint
from Routes.customerBP import customer_blueprint
from Routes.productBP import product_blueprint
from Routes.productionBP import production_blueprint
from Routes.employeeBP import employee_blueprint


def create_app(config_name):
    app = Flask(__name__)

  
    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)


    app.register_blueprint(order_blueprint, url_prefix='/api/orders')
    app.register_blueprint(customer_blueprint, url_prefix='/api/customers')
    app.register_blueprint(employee_blueprint, url_prefix='/api/employees')
    app.register_blueprint(product_blueprint, url_prefix='/api/products')
    app.register_blueprint(production_blueprint, url_prefix='/api/productions')

    return app


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')  
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
