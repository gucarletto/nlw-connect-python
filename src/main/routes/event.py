from flask import Blueprint, jsonify, request

event_route_bp = Blueprint('event_route', __name__)

from src.validators.events_creator_validator import events_creator_validator
from src.http_types.http_request import HttpRequest
from src.controllers.events.events_creator import EventsCreator
from src.model.repositories.eventos_repository import EventosRepository

@event_route_bp.route('/event', methods=['POST'])
def create_new_event():
  events_creator_validator(request.json)
  http_request = HttpRequest(body=request.json)

  events_creator = EventsCreator(EventosRepository())
  http_response = events_creator.create_event(http_request)

  return jsonify(http_response.body), http_response.status_code