class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = []
        
        for i in range(c+1):
            if i**2 <= c:
                nums.append(i)
            else:
                break
        l=0
        e= len(nums)-1
        while(l <=e):
            if nums[l]**2 + nums[e]**2  < c:
                l+=1
            elif nums[l]**2 + nums[e]**2  == c:
                return True
            else:
                e-=1
        return False
        