from sqlalchemy import Column, Integer, String
from base import Base

class Player(Base):
  __tablename__ = 'player'
  id = Column(Integer, primary_key = True)
  name = Column(String)

  def __repr__(self):
    return "<Player(name='%s')>" %  (self.name)