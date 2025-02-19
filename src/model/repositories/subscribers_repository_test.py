import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip(reason='Insert in db')
def test_insert():
  subscriber_infos = {
    'name': 'John Doe',
    'email': 'test@email.com',
    'link': 'http://test.com',
    'evento_id': 1,
  }
  subscribers_repository = SubscribersRepository()
  subscribers_repository.insert(subscriber_infos)

@pytest.mark.skip(reason='Select in db')
def test_select_subscriber():
  subscriber_email = 'test@email.com'
  subscriber_event_id = 1
  subscribers_repository = SubscribersRepository()
  subscriber = subscribers_repository.select_subscriber(subscriber_email, subscriber_event_id)
  assert subscriber.email == subscriber_email
  assert subscriber.evento_id == subscriber_event_id
