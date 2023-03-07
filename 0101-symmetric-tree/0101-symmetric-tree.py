# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         cur = root
        
#         def helper(right,left):
#             if right is None or left is None:
#                 return True
#             if  right is  None or left is  None:
#                 return False
           
#             if right.val == left.val :
#                 Right = helper(left.right, right.left)

#                 Left = helper(left.left, right.right)

#                 return Left and Right
#             else:
#                 return False
#         return helper(cur.right,cur.left)
            if root is None:
                return True
            else:
                return self.helper(root.left, root.right)

    def helper(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            RightCheck = self.helper(left.left, right.right)
            LeftCheck = self.helper(left.right, right.left)
            return RightCheck and LeftCheck
        else:
            return False



