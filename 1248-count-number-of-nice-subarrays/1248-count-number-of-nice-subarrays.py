class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        sum=0
        predic= defaultdict(int)
        predic={0:1}
        
        for i in range(len(nums)):
            
            if nums[i] %2 ==0:
                nums[i]=0
            else:
                nums[i]=1
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        print(nums)
        for j in range(len(nums)):
            
            if nums[j]- k in predic:
                count += predic[nums[j] - k]
            if nums[j] in predic:
                predic[nums[j]] += 1
            else:
                predic[nums[j]]=1
        return count

            
          