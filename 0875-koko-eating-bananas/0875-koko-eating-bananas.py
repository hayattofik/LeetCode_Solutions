import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
      
        
        l = 1
        r = max(piles)
        output = r
        
        while(l<=r):
            Sum = 0
            mid = l + (r-l)//2
            for pile in piles:
                Sum += math.ceil(pile/mid)
            if Sum > h:
                l = mid +1
            elif Sum <= h:
                output = min(output,mid)
                r = mid - 1
           
        return output
                
            
            
            
        