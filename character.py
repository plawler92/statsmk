from sqlalchemy import Column, Integer, String
from base import Base

class Character(Base):
  __tablename__ = 'character'
  id = Column(Integer, primary_key = True)
  name = Column(String)
  gameid = Column(Integer, ForeignKey('videogame.id'))