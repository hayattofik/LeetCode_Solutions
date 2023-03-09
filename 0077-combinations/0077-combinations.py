class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        output =[]
        def backTracking(lis,num):
            if len(lis) == k:
                output.append(lis.copy())
                return 
            
            for i in range(num,n+1):
                
                # place
                lis.append(i)
                
                #backtrack
                backTracking(lis,i+1)
                
                #remove
                lis.pop()
    
                    
        backTracking([],1)
        return output
            
        
        