from src.main.routes.event import event_route_bp
from src.main.routes.subscriptions import subscription_route_bp
from src.main.routes.events_link import events_link_route_bp
from flask import Flask

app = Flask(__name__)

app.register_blueprint(event_route_bp)
app.register_blueprint(subscription_route_bp)
app.register_blueprint(events_link_route_bp)