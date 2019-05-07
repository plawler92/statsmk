from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Match(Base):
  __tablename__ = 'match'
  id = Column(Integer, primary_key = True)
  eventid = Column(Integer)
  matchtypeid = Column(Integer)

  games = relationship('Game')

  #gameid = Column(Integer, ForeignKey('videogame.id'))

  #def __repr__(self):
    #return "<Match(name='%s'='%s')>" %  (self.name, self.variation)