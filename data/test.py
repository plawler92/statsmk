#data = smash.get_page_of_sets(eventSlug, page, perPage)
import json

data = {}

with open('smashdata-29.json') as f:
  data = json.load(f)

sets = data['sets']['nodes']

games = []
totalcounter = 0
withgamescounter = 0
withoutgamescounter= 0

if sets is None:
  print("NO SETS")

for s in sets:
  totalcounter = totalcounter + 1
  if s['games']  is not None:
    withgamescounter = withgamescounter + 1
    setgames = []
    setid = s['id']
    p1id = s['slots'][0]['standing']['entrant']['id']
    p1name = s['slots'][0]['standing']['entrant']['name']
    p2id = s['slots'][1]['standing']['entrant']['id']
    p2name = s['slots'][1]['standing']['entrant']['name']

    for game in s['games']:
      setgames.append(game['id'])
  else:
    withoutgamescounter = withoutgamescounter + 1
    print("here before slots")
    if s['slots'] is not None:
      print("here after slots")
      for slot in s['slots']:
        print("individual slot")
        eid = slot['standing']['entrant']['id']
        score = slot['standing']['stats']['score']['value']
        for i in range(0, score):
          setgames.append(str(eid) + " " + str(i))

    games.extend(setgames)

print("total: " + str(totalcounter))
print("with: " + str(withgamescounter))
print("without: " + str(withoutgamescounter))