# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def BST(curr,output):
            if curr == None:
                return None
            
            left = BST(curr.left,output)
            output.append(curr.val)
            right = BST(curr.right,output)
            
            return output
        output = []
        curr = root
        ans = BST(curr,output)
        return ans
        