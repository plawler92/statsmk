from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.schema import ForeignKey
from base import Base

class Game(Base):
  __tablename__ = 'game'
  id = Column(Integer, primary_key = True)
  matchid = Column(Integer, ForeignKey('match.id'))
  winnerid = Column(Integer, ForeignKey('player.id'))
  loserid = Column(Integer, ForeignKey('player.id'))
  winnercharacterid = Column(Integer, ForeignKey('character.id'))
  losercharacterid = Column(Integer, ForeignKey('character.id'))
  winnerroundswon = Column(Integer)
  loserroundswon = Column(Integer)

  #gameid = Column(Integer, ForeignKey('videogame.id'))

  #def __repr__(self):
    #return "<Character(name='%s', variation='%s')>" %  (self.name, self.variation)