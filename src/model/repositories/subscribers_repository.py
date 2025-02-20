from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interfaces.subscribers_repository import SubscribersRepositoryInterface
from sqlalchemy import func, desc

class SubscribersRepository(SubscribersRepositoryInterface):
  def insert(self, subscriber_infos: dict) -> None:
    with DBConnectionHandler() as db:
      try:
        new_subscriber = Inscritos(
          nome=subscriber_infos.get('name'),
          email=subscriber_infos.get('email'),
          link=subscriber_infos.get('link'),
          evento_id=subscriber_infos.get('evento_id'),
        )
        db.session.add(new_subscriber)
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception

  def select_subscriber(self, subscriber_email: str, event_id: int) -> Inscritos:
    with DBConnectionHandler() as db:
      return db.session.query(Inscritos).filter_by(email=subscriber_email, evento_id=event_id).first()

  def select_subscribers_by_link(self, link: str, event_id: int) -> list:
    with DBConnectionHandler() as db:
      return db.session.query(Inscritos).filter_by(link=link, evento_id=event_id).all()

  def get_ranking(self, event_id: int) -> tuple:
    with DBConnectionHandler() as db:
      result = (
        db.session.query(
          Inscritos.link,
          func.count(Inscritos.link)).label('total')
        .filter(
          Inscritos.evento_id == event_id,
          Inscritos.link != None
        )
        .group_by(Inscritos.link)
        .order_by(desc('total'))
        .all()
      )