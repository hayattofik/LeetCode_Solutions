class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new=[0]*len(nums)
        for ele in range( len(nums)):
            curidx=(ele + k)%len(nums)
            new[curidx]=nums[ele]
        for  i in range(len(nums)):
            nums[i]=new[i]
            