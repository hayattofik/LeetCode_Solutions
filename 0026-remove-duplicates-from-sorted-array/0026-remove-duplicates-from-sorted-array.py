class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nu_point=0
        check=1
        while(check < len(nums)):
            if nums[check]==nums[nu_point]:
                check+=1
            else:
                nums[nu_point+1]=nums[check]
                nu_point+=1
      
        return nu_point+1
        