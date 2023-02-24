class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        checkDic={}
        output=[]
        for i in range(len(nums2)):
            
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                checkDic[val]= nums2[i]
               
            stack.append(nums2[i])
        
      
        for i in range(len(nums1)):
            if nums1[i] in checkDic:
                output.append(checkDic[nums1[i]])
            else:
                output.append(-1)
        return output
        