# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        if curr == None:
            return None
        if curr.val == val:
            return curr
        
        if curr.val > val :
            left = self.searchBST(curr.left,val)
            return left
        elif curr.val < val:
            
            right = self.searchBST(curr.right,val)
            return right
       