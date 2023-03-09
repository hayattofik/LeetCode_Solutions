# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        que = deque()
        
        que.append(root)
        output = []
        
        while que:
            sub = []
            size = len(que)
            
            for i in range(size):
                
                node = que.popleft()
                if node:
                    que.append(node.left)
                    que.append(node.right)
                    sub.append(node.val)
            if sub:
                output.append(sub)
        return output
                
                    
            
            
            
        
    
            
        