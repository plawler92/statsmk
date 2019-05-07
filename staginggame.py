from sqlalchemy import Column, Integer, String
from base import Base

class StagingGame(Base):
	__tablename__ ='game'
	__table_args__ = {"schema": "staging"}
	id = Column(Integer, primary_key = True)
	eventId = Column(String)
	eventSlug = Column(String)
	eventName = Column(String)
	eventDate = Column(Integer)
	setId = Column(Integer)
	gameId = Column(Integer)
	winnerId = Column(Integer)
	winnerName = Column(String)
	loserId = Column(Integer)
	loserName = Column(String)
	winnerCharacterId = Column(Integer)
	loserCharacterId = Column(Integer)
	sourceId = Column(Integer)

	def __str__(self):
		return f"{self.eventId},{self.eventSlug},{self.eventName},{self.eventDate},{self.setId},{self.gameId},{self.winnerId},{self.winnerName},{self.loserId},{self.loserName},{self.winnerCharacterId},{self.loserCharacterId}"

	def __repr__(self):
		return f"Game:({self.gameId},{self.winnerId},{self.loserId})"