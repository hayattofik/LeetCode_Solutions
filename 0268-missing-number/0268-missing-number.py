class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.output=-1
        
        for i in range(len(nums)+1):
            if i in nums:
                continue
            else:
                self.output=i
                
        return self.output
