from src.model.repositories.interfaces.susbscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersCreator:
  def __init__(self, subscribers_repository: SubscribersRepositoryInterface):
    self.__subs_repo = subscribers_repository

  def create_subscription(self, http_request: HttpRequest) -> HttpResponse:
    subscriber_infos = http_request.body
    self.__check_subscription(subscriber_infos)
    self.__insert_subscription(subscriber_infos)
    return self.__format_response(subscriber_infos)

  def __check_subscription(self, subscriber_infos: dict) -> None:
    exists = self.__subs_repo.select_subscriber(subscriber_infos['email'], subscriber_infos['event_id'])
    if exists:
      raise Exception('Subscription already exists')

  def __insert_subscription(self, subscriber_infos: dict) -> None:
    self.__subs_repo.insert(subscriber_infos)

  def __format_response(self, subscriber_infos: dict) -> HttpResponse:
    return HttpResponse(body={'message': f'User {subscriber_infos.email} subscribed to event {subscriber_infos.event_id}'}, status_code=201)