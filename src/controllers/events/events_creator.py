from src.model.repositories.interfaces.eventos_repository import EventosRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventsCreator:
  def __init__(self, eventos_repository: EventosRepositoryInterface):
    self.__events_repo = eventos_repository

  def create_event(self, http_request: HttpRequest) -> HttpResponse:
    event_name = http_request.body['name']
    self.__check_event(event_name)
    self.__insert_event(event_name)
    return self.__format_response(event_name)

  def __check_event(self, event_name: str) -> None:
    exists = self.__events_repo.select_event(event_name)
    if exists:
      raise Exception('Event already exists')

  def __insert_event(self, event_name: str) -> None:
    self.__events_repo.insert(event_name)

  def __format_response(self, event_name: str) -> HttpResponse:
    return HttpResponse(body={'message': f'Event {event_name} created successfully'}, status_code=201)