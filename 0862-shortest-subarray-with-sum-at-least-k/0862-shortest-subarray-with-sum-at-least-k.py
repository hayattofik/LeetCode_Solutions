from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSum = [0]
        ans =len(nums)+1
        for n in nums:
            preSum.append(n+preSum[-1])
        qeue = deque()
        
     
        for r,let in enumerate(preSum):
            
            while(qeue and let <= preSum[qeue[-1]]):
               
                    qeue.pop()
              
               
            while qeue  and let - preSum[qeue[0]] >=k:
                i = qeue.popleft()
                ans = min(ans,r-i)
            qeue.append(r)
            
        if ans == len(nums) +1:
            return -1 
        else:
            return ans
        
                
            
       
    