class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l,r = max(weights),sum(weights)
        res = r
        
        def canShip(curCap):
            needShip = 1
            cap = curCap
            
            for weight in weights:
                if cap - weight < 0:
                    needShip +=1
                    cap = curCap
                cap -=weight
                
            return  needShip <= days
        
        while(l<=r):
            curCap =(l + r)//2
            
            if canShip(curCap):
                res = min(res,curCap)
                r = curCap -1
            else:
                l = curCap + 1
        return res
        
        