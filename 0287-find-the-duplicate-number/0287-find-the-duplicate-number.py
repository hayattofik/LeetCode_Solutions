class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        output =[]
        #sort
        
        pivot = 0
        while(pivot < len(nums)):
            
            temp = nums[pivot] -1
            if temp < len(nums) and nums[pivot] != nums[temp]:
                nums[pivot],nums[temp] = nums[temp],nums[pivot]
            else:
                pivot +=1
        for i in range(len(nums)):
            if i +1 != nums[i]:
                return nums[i]
       
        