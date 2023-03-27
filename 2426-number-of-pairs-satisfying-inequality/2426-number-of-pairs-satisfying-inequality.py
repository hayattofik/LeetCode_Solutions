class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n=len(nums1)
        for i in range(n):
            nums1[i]=nums1[i]-nums2[i]
        ans=0
        arr=[]
        for i in range(n):
            x=bisect_right(arr,nums1[i]+diff)
            ans+=x
            insort(arr,nums1[i])
        return ans
        