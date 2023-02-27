class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ReferSum =[0]
        for i  in range(len(self.nums)):
            s = self.nums[i] + self.ReferSum[i]
            self.ReferSum.append(s)
        
        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.ReferSum[right+1]
        else:
            output = self.ReferSum[right+1] - self.ReferSum[left]
            return output
       
        
        
            
            
       
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)