class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pivot = 0
        
        n = len(nums)
        if n not in nums:
            return n
        
        while(pivot < len(nums)):
            if nums[pivot] != pivot:
                # temp = 
                if nums[pivot] < len(nums):

                    nums[nums[pivot]],nums[pivot] = nums[pivot],nums[nums[pivot]]
                else:
                    pivot +=1
            # else:
            else:
                pivot +=1
      
        for i in range(len(nums)):
           
            if i != nums[i]:
                
                return i
            