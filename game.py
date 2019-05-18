from sqlalchemy import Column, Integer, String
from base import Base

class Game(Base):
	__tablename__ ='game'
	__table_args__ = {"schema": "public"}
	id = Column(Integer, primary_key = True)
	eventid = Column(String)
	eventslug = Column(String)
	eventname = Column(String)
	eventdate = Column(Integer)
	setid = Column(Integer)
	gameid = Column(Integer)
	winnerid = Column(Integer)
	winnername = Column(String)
	loserid = Column(Integer)
	losername = Column(String)
	winnercharacterid = Column(Integer)
	losercharacterid = Column(Integer)
	sourceid = Column(Integer)
	setgametype = Column(String)
	winnercharactername = Column(String)
	losercharactername = Column(String)

	def __str__(self):
		return f"{self.eventid},{self.eventslug},{self.eventname},{self.eventdate},{self.setid},{self.gameid},{self.winnerid},{self.winnername},{self.loserid},{self.losername},{self.winnercharacterid},{self.losercharacterid}"

	def __repr__(self):
		return f"Game:({self.gameid},{self.winnerid},{self.loserid})"