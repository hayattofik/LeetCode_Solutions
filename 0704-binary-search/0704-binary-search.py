class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binaryHelper(l,r,target):

            if l > r:
                return -1
            
            mid = l + (r-l)//2
            
            if nums[mid] < target:
                return binaryHelper(mid+1,r,target)
            elif nums[mid] > target:
                return binaryHelper(l,mid -1,target)
            else:
                return mid
        return binaryHelper(0,len(nums)-1,target)
