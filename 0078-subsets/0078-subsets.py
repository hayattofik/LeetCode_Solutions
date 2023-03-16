class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def helper(cur, lis):
            
            if cur == len(nums):
                return
            
            
            for  i in range(cur,len(nums)):
                
                #place
                lis.append(nums[i])
                output.append(lis.copy())
                
                # backtrack
                helper(i+1,lis)
                
                #remove
                
                lis.pop()
                
                
            return output
        output.append([])
        return helper(0,[])
                
        