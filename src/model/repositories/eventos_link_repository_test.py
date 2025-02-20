import pytest
from src.model.repositories.eventos_link_repository import EventosLinkRepository

@pytest.mark.skip(reason='Insert in db')
def test_insert():
  event_id = 1
  subscriber_id = 1
  eventos_link_repository = EventosLinkRepository()
  link = eventos_link_repository.insert(event_id, subscriber_id)
  assert link is not None

@pytest.mark.skip(reason='Select in db')
def test_select_events_link():
  event_id = 1
  subscriber_id = 1
  eventos_link_repository = EventosLinkRepository()
  event_link = eventos_link_repository.select_events_link(event_id, subscriber_id)
  assert event_link is not None
  assert event_link.evento_id == event_id
  assert event_link.inscrito_id == subscriber_id