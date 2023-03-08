# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root  
        self.cnt = 0
        self.ans = 0
        
        def Traverse(cur):
            
            if cur == None:
                
                return None
            
            Traverse(cur.left)
            self.cnt +=1
            if self.cnt == k:
                self.ans = cur.val
            
            Traverse(cur.right)
       
        Traverse(cur)
      
        return self.ans