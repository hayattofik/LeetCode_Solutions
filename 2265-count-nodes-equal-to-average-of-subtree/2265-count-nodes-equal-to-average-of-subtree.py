# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        count = 0
        def preOrder(cur):
            if cur == None:
                return [0,0]
            '''the first elememt in the  array contains the 
            count of nodes where as the second holds there sum ''' 
            Left = preOrder(cur.left)
            Right = preOrder (cur.right)
            
            
            nodes = Left[0] +Right[0] + 1
            Sum = Left[1] + Right[1] + cur.val
            
            Average = Sum//nodes
            if Average == cur.val:
                nonlocal count
                count +=1
            return [nodes,Sum]
        
        preOrder(root)
        
        return count
        