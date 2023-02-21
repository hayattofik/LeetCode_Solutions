# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        check =[]
        while cur:
            check.append(cur)
            cur = cur.next
        l=0
        r=0
        for i in range(len(check)):
            if i ==left-1:
                l= i
            elif i == right-1:
                r= i
            
        while(l <= r):
            check[l],check[r] = check[r],check[l]
            l+=1
            r-=1
        output = ListNode()
        cur = output
        for i in range(len(check)-1):
            cur.next = check[i]
            cur = cur.next
        check[-1].next = None
        cur.next = check[-1]
        return output.next
            
        
       