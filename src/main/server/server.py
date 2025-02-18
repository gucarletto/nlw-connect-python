from src.main.routes.event import event_route_bp
from flask import Flask

app = Flask(__name__)

app.register_blueprint(event_route_bp)