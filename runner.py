import db as d
import smashtest as s
import datahandler as dh

#dh.insert_games(d.session, s.games)
games = []
#games.extend(s.get_games(s.eventSlug, 1, 50))

#759 total
for i in range(1, 40):
  try:
    games.extend(s.get_games(s.eventSlug, i, 25))
  except:
    print(i)

def test(i):
  try:
    games.extend(s.get_games(s.eventSlug, i, 25))
  except Exception as e:
    print(i)
  #print(i)

#dh.insert_games(d.session, games)