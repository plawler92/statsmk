from smashggAPI import client

#step 1, find out how many sets are in an event
#eventId = 347685
eventSlug = "tournament/kombat-cup-road-to-combo-breaker/event/kombat-cup"
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









