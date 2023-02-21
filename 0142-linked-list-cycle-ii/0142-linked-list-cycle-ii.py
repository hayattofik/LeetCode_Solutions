# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checkCycle= defaultdict(int)
       
        cur = head 
        check = 0
        while cur:
            if checkCycle[cur] < 1:
                checkCycle[cur]+=1
            else:
                check = cur 
                return cur
            cur = cur.next
       
            
        return None
        