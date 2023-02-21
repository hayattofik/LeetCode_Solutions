# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checkCycle=set()
       
        cur = head 
        check = 0
        while cur:
            if cur not in checkCycle:
                checkCycle.add(cur)
            else:
                
                return cur
            cur = cur.next
       
            
        return None
        