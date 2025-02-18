import pytest
from .eventos_repository import EventosRepository

@pytest.mark.skip(reason='Insert in db')
def test_insert_eventos():
  event_name = 'Event Test'
  repository = EventosRepository()
  repository.insert(event_name)

@pytest.mark.skip(reason='Select in db')
def test_select_eventos():
  event_name = 'Event Test'
  repository = EventosRepository()
  event = repository.select_event(event_name)
  assert event.nome == event_name