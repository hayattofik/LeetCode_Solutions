class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for j in range(len(nums)-1):
            flag=0
            for i in range(len(nums)-1-j):
                if nums[i]>nums[i+1]:
                    nums[i+1],nums[i]=nums[i],nums[i+1]
                    flag=1
            if flag==0:
                break
       