class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count=0
        # start=0
        # end=start+1
        # while(start<len(nums)-1):
        #     if end ==len(nums)-1:
        #         start+=1
        #         end=start+1

        #     else:
        #         if nums[start]==nums[end]:
        #             count+=1
                    
        #         end+=1
        # return count
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
        return count
     
                
                
            

