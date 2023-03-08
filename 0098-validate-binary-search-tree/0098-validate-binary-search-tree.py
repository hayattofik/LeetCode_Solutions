# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur = root
        def check_validate(root, lower, upper):
          
            if not root:
                return True
            if lower >= root.val or upper <= root.val:
                return False
            else:
                Left = check_validate(root.left, lower, root.val) 
                Right = check_validate(root.right, root.val, upper)
                return Left and Right
            
        return check_validate(root, -math.inf, math.inf)
        