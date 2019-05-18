import db.db as d
from db.staginggame import StagingGame
from db.character import Character
import json

def create_tables():
  d.Base.metadata.create_all(d.engine)

def load_characters():
  characters = []
  with open('data/characters.json') as f:
    data = json.load(f)
  for c in data['entities']['character']:
    #for mortal kombat 11 only right now
    if c['videogameId'] == 3200:
      nc = Character()
      nc.name = c['name']
      nc.videogameid = c['videogameId']
      nc.characterid = c['id']
      characters.append(nc)
  for character in characters:
    d.session.add(character)
  d.session.commit()

if __name__ == "__main__":
  create_tables()
  load_characters()