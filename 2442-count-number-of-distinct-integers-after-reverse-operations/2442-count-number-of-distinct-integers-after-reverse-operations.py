class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
     
        Set = set(nums)
        for n in nums:
            strN = str(n) 		
            strR = strN[::-1] 	
            Set.add(int(strR))
       
        return len(Set)
        