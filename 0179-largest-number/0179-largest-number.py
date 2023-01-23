class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strmap={}
        for i in range(len(nums)):
            strmap[nums[i]]=str(nums[i])

        output = ''
        if sum(nums)==0:
            return str(0)
        else:
            for i in range(len(nums)):
                for j in range(len(nums)-1):
                    if strmap[nums[j]] + strmap[nums[j+1]] > strmap[nums[j+1] ]+ strmap[nums[j]]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
                
                output+=strmap[nums[len(nums)-i-1]]
            
            return output
                    
            
            