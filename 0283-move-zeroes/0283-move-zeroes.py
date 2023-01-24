class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_pointer=0
        p_pointer=0
        for i in range(len(nums)):
            if nums[i]==0:
                z_pointer=i
                p_pointer=i+1
                break
        while(p_pointer<len(nums)):
            if nums[p_pointer] !=0:
                nums[z_pointer],nums[p_pointer]=nums[p_pointer],nums[z_pointer]
                z_pointer+=1
                p_pointer+=1
            else:
                p_pointer+=1
        return nums
        
        