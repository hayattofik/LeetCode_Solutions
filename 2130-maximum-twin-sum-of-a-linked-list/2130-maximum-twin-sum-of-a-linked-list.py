# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lis=[]
        while(head):
            lis.append(head.val)
            head = head.next
        e=len(lis)-1
        s= 0
        MaxSum=0
        while(s < e):
            temp= lis[s] + lis[e]
            MaxSum = max(MaxSum,temp)
            s+=1
            e-=1
        return MaxSum
            
        