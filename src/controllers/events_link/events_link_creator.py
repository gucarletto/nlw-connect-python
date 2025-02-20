from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.eventos_link_repository import EventosLinkRepository

class EventsLinkCreator:
  def __init__(self, events_link_repository: EventosLinkRepository):
      self.__events_link_repository = events_link_repository

  def create(self, request: HttpRequest) -> HttpResponse:
    event_id = request.body['event_id']
    sub_id = request.body['subscriber_id']

    self.__check_event_link(event_id, sub_id)
    new_link = self.__create_event_link(event_id, sub_id)

    return self.__format_response(new_link)

  def __check_event_link(self, event_id: int, subscriber_id: int) -> None:
    response = self.__events_link_repository.select_events_link(event_id, subscriber_id)
    if response:
      raise Exception('Link already exists')

  def __create_event_link(self, event_id: int, subscriber_id: int) -> str:
    return self.__events_link_repository.insert(event_id, subscriber_id)

  def __format_response(self, link: str) -> HttpResponse:
    return HttpResponse(201, {'link': link})