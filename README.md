# statsmk
Graph QL Queryies
set score
query set($setId: ID!){
  set(id:$setId){
    id
    slots{
      standing{
        placement
        entrant{
          name
        }
        stats{
          score {
            label
            value
          }
        }
      }
    }
  }
}
20103032

query EventSets($eventSlug: String!, $page:Int!, $perPage:Int!){
  event(slug:$eventSlug){
    id
    slug
    name
    sets(
      page: $page
      perPage: $perPage
      sortType: STANDARD
    ){
      pageInfo{
        total
      }
      nodes{
        id
        slots{
          id
          standing{
            placement
            entrant{
              id
              name
            }
            stats{
              score{
                label
                value
              }
            }
          }
          entrant{
            id
            name
          }
        }
      }
    }
  }
}

{
  "eventSlug": "tournament/kombat-cup-road-to-combo-breaker/event/kombat-cup",
  "page":13,
  "perPage":1
}
