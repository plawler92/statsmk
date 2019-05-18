import db as d
import smashtest as s
import datahandler as dh
import plotly.plotly as py
import plotly.graph_objs as go

kombatcup = "tournament/kombat-cup-road-to-combo-breaker/event/kombat-cup"
#summit = "tournament/summit-of-time/events/mortal-kombat-11"
summit = "tournament/summit-of-time/event/mortal-kombat-11"

#dh.insert_games(d.session, s.games)
games = []
#games.extend(s.get_games(s.eventSlug, 1, 50))

#759 total
def test1():
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

def load_and_insert_by_eventslug(eventSlug):
  data = []
  for i in range(1, 40):
    data.extend(s.get_games(eventSlug, i , 25))
  dh.insert_games(d.session, games)

#dh.insert_games(d.session, games)

def get_winlossrates(eventid = 0):
  games = dh.get_games(d.session)
  stats = {}
  for game in games:
    if game.winnercharactername in stats.keys():
      stats[game.winnercharactername]['wins'] += 1
    else:
      stats[game.winnercharactername] = {'wins': 1, 'loss': 0}

    if game.losercharactername in stats.keys():
      stats[game.losercharactername]['loss'] += 1
    else:
      stats[game.losercharactername] = {'wins': 0, 'loss': 1}
  
  return stats

def plot_winlossrates(stats, name):
  names = []
  wins = []
  losses =[]
  for item in stats.items():
    if item[0] != 'UNKNOWN':
      names.append(item[0])
      wins.append(item[1]['wins'])
      losses.append(item[1]['loss'])
  
  trace1 = go.Bar(x = names, y = wins, name = 'wins')
  trace2 = go.Bar(x = names, y = losses, name = 'loss')

  data = [trace1, trace2]
  layout = go.Layout(barmode = 'group')
  fig = go.Figure(data=data, layout=layout)
  py.plot(fig, filename = name)
  
#dh.insert_games(d.session, games)
#def insert_games(session, games):
#  for game in games:
#    session.add(game)
#  session.commit()
