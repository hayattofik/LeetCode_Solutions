# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left 
            
            curr  =root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val 
            root.right = self.deleteNode(root.right,root.val)
        return root
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
##         def get_min(curr):
                     
#             while(curr.left  != None):
#                 curr = curr.left
#             return curr
#             left = get_min(curr.left)
#             return left
#         def search(cur,val):
#             if cur == None:
#                 return None
#             if cur.val == val:
#                 return cur



#             if cur.val < val:
#                 right = search(cur.right,key)
#                 return right

#             elif cur.val  > val :
#                 left = search(cur.left,key)
#                 return left
#         curr = root
#         value = search(curr,key)
#         # return the right node from the node to be deleted
#         if value:
#             value2 = value.right

#             # print(value2)
#             # get the minimum value to be swapped with it 
#             toSwap = get_min(value2)
#             print(toSwap)
#             value.val = toSwap.val
#             toSwap = self.deleteNode(toSwap.right,key)
#         return root




