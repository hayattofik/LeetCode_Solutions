class Solution:
    def valid_triangle(self,a,b,c):
        if b+c> a:
            return True
        # elif a + c > b :
        #     return True
        # elif b+c > a:
        #     return True
        else:
            return False
    def largestPerimeter(self, nums: List[int]) -> int:
        max_sum=0
        if len(nums) < 3 :
            return 0
        nums.sort()
        s1= len(nums) -1
        s2=s1-1
        s3 = s2-1
        temp=0
        while(s3 >=0):
            if self.valid_triangle(nums[s1],nums[s2],nums[s3]):
                temp = temp + nums[s1]+ nums[s2] + nums[s3]
                # max_sum = max(temp, max_sum)
                return temp
            
            s1-=1
            s2-=1
            s3-=1
        return 0
        
                
#         if max_sum == 0:
#             return 0
#         else:
#             return max_sum
        