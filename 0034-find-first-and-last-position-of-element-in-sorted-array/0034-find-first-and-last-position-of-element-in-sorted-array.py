class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l,r = 0,len(nums)-1
        b =-1
        e =-1
        
        while(l <= r):
           
            mid = (l+r)//2
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid -1
            else:

                r = mid
                while(mid>=0 and nums[mid]==target ):
                    mid-=1
                b = mid +1
                while(r < len(nums) and nums[r]==target):
                    r +=1
                e = r-1
                return [b,e]
        return [b,e]
                    
                
                
                
        