class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        gr = []
        output =[]
        pivots=[]
        for num in nums:
            if num  < pivot:
                less.append(num)
            elif num == pivot:
                pivots.append(num)
            else:
                gr.append(num)
                
        output = less + pivots + gr
        
        return output
        