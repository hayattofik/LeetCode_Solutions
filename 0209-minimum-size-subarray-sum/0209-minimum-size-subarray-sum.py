class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minArray = float('inf')
       
        right =0
        left =0
        cur =0
        while(right< len(nums)):
            cur +=nums[right]
           
            while(cur >= target):   
                minArray = min(minArray,right-left+1)
                cur -=nums[left]
                left +=1
            right+=1
           
            
         
        if minArray == float('inf'):
            return 0
        return minArray