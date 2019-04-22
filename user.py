from sqlalchemy import Column, Integer, String
from base import Base

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key = True)
  name = Column(String)

  def __repr__(self):
    return "<User(name='%s')>" %  (self.name)