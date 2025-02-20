from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscriberManager:
  def __init__(self, subscribers_repository: SubscribersRepositoryInterface):
    self.__subscribers_repository = subscribers_repository

  def get_subscribers_by_link(self, request: HttpRequest) -> HttpResponse:
    link = request.params['link']
    event_id = request.body['event_id']
    subscriber = self.__subscribers_repository.select_subscribers_by_link(link, event_id)
    return self.__format_subs_by_link(subscriber)

  def get_ranking(self, request: HttpRequest) -> HttpResponse:
    event_id = request.body['event_id']
    ranking = self.__subscribers_repository.get_ranking(event_id)
    return self.__format_ranking(ranking)

  def __format_subs_by_link(self, subscribers: list) -> HttpResponse:
    formatted_subs = []
    for subscriber in subscribers:
      formatted_subs.append({
        'name': subscriber.nome,
        'email': subscriber.email
      })
    return HttpResponse(formatted_subs, 200)

  def __format_ranking(self, ranking: list) -> HttpResponse:
    formatted_ranking = []
    for position in ranking:
      formatted_ranking.append({
        'link': position.link,
        'total': position.total
      })
    return HttpResponse(formatted_ranking, 200)