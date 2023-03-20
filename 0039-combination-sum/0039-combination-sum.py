class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        
        def dfs(ptr,lis,Sum):
            
            
            
            if Sum == target:
                self.output.append(lis.copy())
                return 
            if ptr >= len(candidates) or Sum > target:
                return 
            
            lis.append(candidates[ptr])
            
            dfs(ptr,lis,Sum + candidates[ptr])
            
            lis.pop()
            dfs(ptr + 1,lis ,Sum)
            
        dfs(0,[],0)
        return self.output
        