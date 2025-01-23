from flask import Flask
from app.controllers.flower_controller import flower

def create_app():
    app = Flask(__name__)
    app.register_blueprint(flower)
    return app