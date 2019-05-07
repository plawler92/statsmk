from sqlalchemy import Column, Integer, String
from db.db import Base

class Character(Base):
  __tablename__ = 'character'
  id = Column(Integer, primary_key = True)
  name = Column(String)
  videogameid = Column(Integer)
  characterid = Column(Integer)
