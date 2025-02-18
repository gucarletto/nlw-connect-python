from src.model.config.base import Base
from sqlalchemy import Column, Integer, ForeignKey, String

class EventosLink(Base):
  __tablename__ = 'EventosLink'
  id = Column(Integer, primary_key=True, autoincrement=True)
  evento_id = Column(Integer, ForeignKey('Eventos.id'), nullable=False)
  inscrito_id = Column(Integer, ForeignKey('Inscritos.id'), nullable=False)
  link = Column(String, nullable=False)