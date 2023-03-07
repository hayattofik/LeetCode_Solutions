# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        curr = root
        if curr == None:
            return TreeNode(val)
        
        if curr.val > val:
            curr.left = self.insertIntoBST(curr.left,val)
           
        elif curr.val < val:
            curr.right = self.insertIntoBST(curr.right,val)
           
        return curr
        