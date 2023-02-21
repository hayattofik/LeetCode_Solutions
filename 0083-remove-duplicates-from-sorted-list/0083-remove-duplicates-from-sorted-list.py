# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head 
        if head == None :
            return head
        check = cur.next 
        while(check):
            if cur.val == check.val:
                cur.next = check.next
                check = cur.next
            else:
                cur= cur.next
                check = cur.next 
        return head
            
    