class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0
        for value in range(m,len(nums1)):
            nums1[value] = nums2[i]
            i+=1
        start=0
        end = m
        
#         while(end< len(nums1)-1):
#             if nums1[start] > nums1[end]:
#                 nums1[start],nums1[end] = nums1[end] , nums1[start]
#             start+=1
#             if start==end:
#                 start=0
#                 end+=1
#         return nums1
        return nums1.sort()
        
       
    