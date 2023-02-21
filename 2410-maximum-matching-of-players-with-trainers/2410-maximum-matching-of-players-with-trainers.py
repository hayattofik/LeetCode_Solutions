class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        P=0
        T=0
        count=0
        while(P< len(players) and T < len(trainers)):
            if players[P] <= trainers[T]:
                count+=1
                P+=1
            T+=1
        return count
    
        
       
      
        