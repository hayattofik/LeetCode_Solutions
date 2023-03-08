# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def check (cur ,prev ,refer):
            if cur == None:
                return None
            
            refer[cur.val]+=1
            
            check(cur.left,cur.val,refer)
            check(cur.right,cur.val,refer)
            return refer
        ans = defaultdict(int)
    
        check(root,None,ans)
        print(ans)
        output = []
        num = max(ans.values())
      
        
        for key in ans :
            if ans[key] == num:
                output.append(key)
        return output
                
        