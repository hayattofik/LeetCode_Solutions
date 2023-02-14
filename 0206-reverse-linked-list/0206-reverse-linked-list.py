# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # lis =[]
        prev=None
        while(head):
            nxt=head.next
            head.next=prev
            prev=head
            head=nxt
        return prev
        
#         itr = head
#         while(itr):
#             lis.append(itr)
#             itr = itr.next
       
        
#         lis.reverse()
#         for i in range(len(lis)-1):
#             if i == len(lis)-1:
#                  lis[i].next = None
#             else:
                
#                 lis[i].next = lis[i+1]
            
#         return lis
            
            
        