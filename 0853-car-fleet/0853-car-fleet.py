class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        combined = [[p,s] for p,s in zip(position,speed)]
        stack =[]
        
        for p,s in sorted(combined)[::-1]:
            
            val = (target-p)/s
            stack.append(val)
            if len(stack) >=2 and stack[-1] <=stack[-2]:
                stack.pop()
        return len(stack)
                
            
            
        
       
        