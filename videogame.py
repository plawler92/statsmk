from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Videogame(Base):
  __tablename__ = 'videogame'
  id = Column(Integer, primary_key = True)
  name = Column(String)
  
  characters = relationship('character')