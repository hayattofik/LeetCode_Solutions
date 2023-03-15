# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(prev,cur):
            
            if not cur:
                return prev
            
            next_node = cur.next
            cur.next = prev
            return helper(cur,next_node)
            
        return helper(None,head)
        