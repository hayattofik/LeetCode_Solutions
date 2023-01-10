class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        output = []
        pos=[]
        ne = []
        for num in nums:
            if num >=0:
                pos.append(num)
            else:
                ne.append(num)
        ptr=0
        while(ptr<len(pos)):
            output.append(pos[ptr])
            output.append(ne[ptr])
            ptr +=1
        return output
            
              
        
          
        return output
        