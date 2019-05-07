from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.schema import ForeignKey
from base import Base

class Character(Base):
  __tablename__ = 'character'
  id = Column(Integer, primary_key = True)
  name = Column(String)
  variation = Column(String, nullable = True)
  istournament = Column(Boolean)

  gameid = Column(Integer, ForeignKey('videogame.id'))

  def __repr__(self):
    return "<Character(name='%s', variation='%s')>" %  (self.name, self.variation)