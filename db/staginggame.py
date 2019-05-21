from sqlalchemy import Column, Integer, String
from db.db import Base

class StagingGame(Base):
	__tablename__ ='game'
	__table_args__ = {"schema": "staging"}
	id = Column(Integer, primary_key = True)
	eventid = Column(String)
	eventslug = Column(String)
	eventname = Column(String)
	eventdate = Column(Integer)
	setid = Column(Integer)
	setgametype = Column(String)
	gameid = Column(Integer)
	winnerid = Column(Integer)
	winnername = Column(String)
	loserid = Column(Integer)
	losername = Column(String)
	winnercharacterid = Column(Integer)
	losercharacterid = Column(Integer)
	sourceid = Column(Integer)