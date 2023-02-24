class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixdic={0:1}
        counter=0
        sum=0
       
        

        for i in range(len(nums)):
            sum+=nums[i]
            if sum-k in prefixdic:
                counter+=prefixdic[sum -k]
            if sum in prefixdic:
                prefixdic[sum]+=1
            else:
                prefixdic[sum]=1
            
        return counter
       
        