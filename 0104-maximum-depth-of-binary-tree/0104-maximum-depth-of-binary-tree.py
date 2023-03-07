# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        def BSTHelper(curr, depth):
            if curr == None:
                return depth
            
        
            left = BSTHelper(curr.left,depth+1)
            right = BSTHelper(curr.right,depth+1)
            
            return max(left,right)
        return BSTHelper(curr,0)
        