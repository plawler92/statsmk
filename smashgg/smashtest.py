from smashggAPI import client

#step 1, find out how many sets are in an event
#eventId = 347685
eventSlug = "tournament/kombat-cup-road-to-combo-breaker/event/kombat-cup"
eventSlug2 = "tournament/summit-of-time/events/mortal-kombat-11"
games = []
notadded = []

def get_sets_per_event(eventId):
	results = client.query('''
		query EventSets($eventId: ID!, $page: Int!, $perPage: Int!){
			event(id: $eventId){
			id
			name
			sets(page: $page, perPage: $perPage, sortType:STANDARD){
			  pageInfo{
			    total
			  }
			  nodes{
			    id
			    slots{
			      id
			      entrant{
			        id
			        name
			      }
			    }
			  }
			}
			}
			}''',
		{
			"eventId": eventId,
			"page": 1,
			"perPage": 1
		})
	#eventId = 347685
	return results['data']['event']['sets']['pageInfo']['total']

def get_page_of_sets(eventSlug, page, perPage):
	results = client.query('''
		query EventSets($eventSlug: String!, $page:Int!, $perPage:Int!){ 
		  event(slug:$eventSlug){ 
		    id 
		    slug 
		    name 
		    startAt
		    sets( page: $page perPage: $perPage sortType: STANDARD ){ 
		      pageInfo{ 
		        total 
		      } 
		      nodes{ 
		        id 
		        games{
		          id
		          setId
		          winnerId
		          selections{
		            id
		            selectionType
		            selectionValue
		            entrantId
		          }
		        }
		        slots{
		          standing{
		            entrant{
		              id
		              name
		            }
		            placement
								stats{
									score{
										label
										value
										displayValue
									}
								}
		          }
		        }
		      } 
		    }
		  }
		}''',
		{
			"eventSlug": eventSlug,
			"page": page,
			"perPage": perPage
		})
	#return results['data']['event']['sets']['nodes']
	return results['data']['event']



#???
def get_games(eventSlug, page, perPage):


	data = get_page_of_sets(eventSlug, page, perPage)

	e = Event(data['id'], data['slug'], data['name'], data['startAt'])

	sets = data['sets']['nodes']

	games = []

	if sets is None:
		return games
		

	for s in sets:
		if s['games']  is not None:
			setgames = []
			setid = s['id']
			p1id = s['slots'][0]['standing']['entrant']['id']
			p1name = s['slots'][0]['standing']['entrant']['name']
			p2id = s['slots'][1]['standing']['entrant']['id']
			p2name = s['slots'][1]['standing']['entrant']['name']

			for game in s['games']:
				g = Game()
				g.eventId = e.id
				g.eventSlug = e.slug
				g.eventName = e.name
				g.eventDate = e.startAt #probably convert this to a date here
				g.setId = setid
				g.gameId = game['id']
				g.winnerId = game['winnerId']
				g.winnerName = p1name if g.winnerId == p1id else p2name
				g.loserId = p2id if g.winnerId == p1id else p1id
				g.loserName = p2name if g.winnerId == p1id else p1name
				if game['selections'] is None:
					g.winnerCharacterId = None
					g.loserCharacterId = None
				else:
					for selection in game['selections']:
						if selection['selectionType'] == 'CHARACTER' and selection['entrantId'] == g.winnerId:
							g.winnerCharacterId = selection['selectionValue']
						else:
							g.loserCharacterId = selection['selectionValue']
				g.sourceId = 1
				setgames.append(g)

			games.extend(setgames)
		#else:
			#notadded.add(s)
	return games

def write_to_file(eventSlug, page, perPage):
	data = get_page_of_sets(eventSlug, page, perPage)
	return data









