# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        if count==n:
            head=head.next
            return head
        temp=head
        prev=None
        for i in range(count-n):
            prev=temp
            temp=temp.next
        if temp.next!=None:
            prev.next=temp.next
        else:
            prev.next=None
        return head
        