from flask import Flask
from config import Config
from extensions import db
from flask_migrate import Migrate

from main_routes import main
from userAuth_routes import authroutes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    db.init_app(app)
    
    Migrate(app, db)

def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(authroutes)
    
if __name__ == '__main__':

    app = create_app()
    app.run('127.0.0.1', 8000, debug=True)
