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
