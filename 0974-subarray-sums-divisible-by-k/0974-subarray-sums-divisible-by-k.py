class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        Sum =0
        MaxLen = 0
        check = {0:1}
        
        preSum =[0]
        for i in range(len(nums)):
            preSum.append(preSum[-1] +nums[i])
            
        for i in range(1,len(preSum)):
            cur = preSum[i]% k 
            if cur in check:
                MaxLen +=check[cur]
                check[cur]+=1
            else:
                check[cur] =1
        return MaxLen
                
      
      