# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.soln =0
        sumCount = defaultdict(int)
        sumCount[0] = 1
        def helper(Sum,cur):
                if not cur:
                    return 
                Sum +=cur.val

                if Sum - targetSum in sumCount:
                    self.soln += sumCount[Sum - targetSum]
                    
                
                
                
                sumCount[Sum]+=1
                
                helper(Sum,cur.left)
                helper(Sum   ,cur.right)
                
                sumCount[Sum]-=1
                
                
                print(Sum)
                
               
              
          

        helper(0,root)
        print(sumCount)
        return self.soln
            
            
            
                
                
            
            
        