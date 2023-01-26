class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start=0
        end=len(height)-1
        Area=0
        currhe=0
        while(end > start):
            
            width=(end-start)
            heightStart=height[start]
            heightend=height[end]
            if heightStart < heightend:
                currhe=heightStart
               
                start+=1
            else:
                currhe=heightend
                end-=1
            AreaTmp=currhe * width
            if AreaTmp > Area:
                Area=AreaTmp
          
           
        return Area

            
                
            
            
        