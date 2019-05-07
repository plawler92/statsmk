
#import smashtest as s
import smashgg.smashtest as smash
from smashgg.event import Event
from db.staginggame import StagingGame as Game
from db.db import session
import json

def get_games(eventSlug, page, perPage):
  data = smash.get_page_of_sets(eventSlug, page, perPage)

  e = Event(data['id'], data['slug'], data['name'], data['startAt'])

  sets = data['sets']['nodes']

  games = []

  if sets is None:
    return games


  for s in sets:
    setgames = []
    setid = s['id']
    p1id = s['slots'][0]['standing']['entrant']['id']
    p1name = s['slots'][0]['standing']['entrant']['name']
    p2id = s['slots'][1]['standing']['entrant']['id']
    p2name = s['slots'][1]['standing']['entrant']['name']
    if s['games']  is not None:
      for game in s['games']:
        g = Game()
        g.eventid = e.id
        g.eventslug = e.slug
        g.eventname = e.name
        g.eventdate = e.startAt #probably convert this to a date here
        g.setid = setid
        g.gameid = game['id']
        g.winnerid = game['winnerId']
        g.winnername = p1name if g.winnerid == p1id else p2name
        g.loserid = p2id if g.winnerid == p1id else p1id
        g.losername = p2name if g.winnerid == p1id else p1name
        if game['selections'] is None:
          g.winnercharacterid = None
          g.losercharacterid = None
        else:
          for selection in game['selections']:
            if selection['selectionType'] == 'CHARACTER' and selection['entrantId'] == g.winnerid:
              g.winnercharacterid = selection['selectionValue']
            else:
              g.losercharacterid = selection['selectionValue']
        g.sourceid = 1
        setgames.append(g)
    else:
      if s['slots'] is not None:
        for slot in s['slots']:
          eid = slot['standing']['entrant']['id']
          score = slot['standing']['stats']['score']['value']
          for i in range(0, score):
            g = Game()
            g.eventid = e.id
            g.eventslug = e.slug
            g.eventname = e.name
            g.eventdate = e.startAt #probably convert this to a date here
            g.setid = setid
            g.winnerid = eid
            g.winnername = p1name if g.winnerid == p1id else p2name
            g.loserid = p2id if g.winnerid == p1id else p1id
            g.losername = p2name if g.winnerid == p1id else p1name
            g.sourceid = 1
            setgames.append(g)

    games.extend(setgames)

  return games

def write_to_file(eventSlug, page, perPage):
    data = smash.get_page_of_sets(eventSlug, page, perPage)
    return data

def populatejson():
  for i in range(1, 40):
    with open(f"data/smashdata-{i}.json", "w") as f:
      #f.write(s.write_to_file(s.eventSlug, i, 25))
      data = write_to_file(smash.eventSlug, i, 25)
      json.dump(data, f)

def populate_aws(start, end, pageSize):
  games = []
  for i in range(start, end):
    try:
      games.extend(get_games(smash.eventSlug, i, pageSize))
    except Exception as e:
      print(e)

  for game in games:
    session.add(game)
  session.commit()

if __name__ == "__main__":
    populate_aws(1, 40, 25)

