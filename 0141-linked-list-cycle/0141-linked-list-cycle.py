# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checkCycle= defaultdict(int)
       
        cur = head 
        while cur:
            if checkCycle[cur] < 1:
                checkCycle[cur]+=1
            else:
                return True
            cur = cur.next
            
        return False