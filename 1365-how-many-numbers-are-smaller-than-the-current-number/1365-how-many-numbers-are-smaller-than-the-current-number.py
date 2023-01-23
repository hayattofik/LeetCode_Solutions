class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lis=[]
        
        for i in nums:
            num = 0
           
            for j in nums:
               
                if j<i:
                
                    num=num+1
            lis.append(num)
        return lis
        