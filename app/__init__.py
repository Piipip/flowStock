from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///inventory.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
    
    CORS(app)
    db.init_app(app)
    ma.init_app(app)
    
    from app.routes import product_routes, sales_routes, report_routes, frontend_routes
    app.register_blueprint(product_routes.bp)
    app.register_blueprint(sales_routes.bp)
    app.register_blueprint(report_routes.bp)
    app.register_blueprint(frontend_routes.bp)
    
    with app.app_context():
        db.create_all()
    
    return app