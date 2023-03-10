class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def Sum(nums,div):
            allSum =0
            for n in nums:
                allSum +=math.ceil(n/div)
            return allSum
                
        
        l,r = 1,max(nums)
        ans = (float('inf'))
        
        while(l <=r):
            mid = (l+r)//2
            
            value = Sum(nums,mid)
            
            if value > threshold:
                l = mid + 1
                
            elif value <= threshold:
                ans = min(ans,mid)
                r = mid -1
        return ans
            
        
        
      
       