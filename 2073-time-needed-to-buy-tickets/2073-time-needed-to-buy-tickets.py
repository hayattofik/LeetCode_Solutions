class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = deque()
        
        for i,tic in enumerate(tickets):
            que.append([i,tic])
            
      
        time = 0
        
        while(que):
            val = que.popleft()
            val[1]-=1
            time +=1
            
            if val[1] ==0 and val[0] == k:
                return time
            elif val[1] != 0:
                que.append(val)
            
            
            
        