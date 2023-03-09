# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        que = deque()
        que.append(root)
        res = []
        while(que):
            size = len(que)
          
            right = que[-1]
            if right:
                res.append(right.val)
            for i in range(size):
                node = que.popleft()
                if node and node.left != None:
                    que.append(node.left)
                if node and node.right!= None:
                    que.append(node.right)
        return res
                
            
        
        
        