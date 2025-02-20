from flask import Blueprint, jsonify, request

subscription_route_bp = Blueprint('suscriptions_route', __name__)

from src.validators.subscribers_creator_validator import subscribers_creator_validator
from src.http_types.http_request import HttpRequest
from src.controllers.subscribers.susbcribers_creator import SubscribersCreator
from src.model.repositories.subscribers_repository import SubscribersRepository
from src.controllers.subscribers.susbcribers_manager import SubscriberManager

@subscription_route_bp.route('/subscription', methods=['POST'])
def create_new_subscription():
  subscribers_creator_validator(request.json)
  http_request = HttpRequest(body=request.json)

  subs_creator = SubscribersCreator(SubscribersRepository())
  http_response = subs_creator.create_subscription(http_request)

  return jsonify(http_response.body), http_response.status_code

@subscription_route_bp.route('/subscription/link/<link>/event/<event_id>', methods=['GET'])
def susbscribers_by_link(link, event_id):
  subs_repo = SubscribersRepository()
  subs_manager = SubscriberManager(subs_repo)

  http_request = HttpRequest(params={'link': link, "event_id": event_id})

  http_response = subs_manager.get_subscribers_by_link(http_request)

  return jsonify(http_response.body), http_response.status_code

@subscription_route_bp.route('/subscription/ranking/event/<event_id>', methods=['GET'])
def susbscribers_link_ranking(event_id):
  subs_repo = SubscribersRepository()
  subs_manager = SubscriberManager(subs_repo)

  http_request = HttpRequest(params={"event_id": event_id})

  http_response = subs_manager.get_ranking(http_request)

  return jsonify(http_response.body), http_response.status_code