class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l= 0
        r =k 
        cur =sum(nums[l:r])
        maxAverage= cur/k
        while(r< len(nums)):
           
            
            cur -=nums[l]
            cur +=nums[r]
            maxAverage= max(maxAverage,cur/k)
            l+=1
            r+=1
        return maxAverage
            
        
        