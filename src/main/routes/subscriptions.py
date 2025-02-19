from flask import Blueprint, jsonify, request

subscription_route_bp = Blueprint('suscriptions_route', __name__)

from src.validators.subscribers_creator_validator import subscribers_creator_validator
from src.http_types.http_request import HttpRequest
from src.controllers.subscribers.susbcribers_creator import SubscribersCreator
from src.model.repositories.subscribers_repository import SubscribersRepository

@subscription_route_bp.route('/subscription', methods=['POST'])
def create_new_subscription():
  subscribers_creator_validator(request.json)
  http_request = HttpRequest(body=request.json)

  subs_creator = SubscribersCreator(SubscribersRepository())
  http_response = subs_creator.create_subscription(http_request)

  return jsonify(http_response.body), http_response.status_code