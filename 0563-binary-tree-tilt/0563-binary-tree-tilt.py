class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0 #global tilt sum
        
        def dfs(node):
            if not node: return 0  # if node is null return 0
            
			# traverse depth wise till we reach the leaf nodes
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            
            self.res += abs(leftSum - rightSum)
            return node.val + leftSum + rightSum # return sum of left and right subtrees
            
        dfs(root)
        return self.res