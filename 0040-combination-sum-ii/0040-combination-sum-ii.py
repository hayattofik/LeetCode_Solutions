class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        candidates.sort()
        
        def backTrack(ptr,lis,Sum):
        
            
            if Sum == target:
                self.output.append(lis.copy())
                return 
            if ptr >= len(candidates) or Sum > target:
                return 
            mainCandidate = -5
            for i in range(ptr,len(candidates)):
                #place
                if candidates[i] == mainCandidate :
                        continue
               
                lis.append(candidates[i])
                # backTrack
               
                backTrack(i + 1,lis,Sum + candidates[i])
                
                # remove
                lis.pop()
                mainCandidate = candidates[i]
                
                
                
                
            
        backTrack(0,[],0)
        return self.output
        