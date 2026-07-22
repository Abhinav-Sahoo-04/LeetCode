# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=l1
        b=l2
        start=None
        temp=start
        carry=0
        while a!=None and b!=None:
            value=a.val+b.val+carry
            term=value%10
            carry=value//10
            node=ListNode(term)
            if start==None:
                start=node
                temp=node
            else:
                temp.next=node
                temp=node
            a=a.next
            b=b.next
        while a!=None:
            value=a.val+carry
            term=value%10
            carry=value//10
            node=ListNode(term)
            if start==None:
                start=node
                temp=node
            else:
                temp.next=node
                temp=node
            a=a.next
        while b!=None:
            value=b.val+carry
            term=value%10
            carry=value//10
            node=ListNode(term)
            if start==None:
                start=node
                temp=node
            else:
                temp.next=node
                temp=node
            b=b.next
        if carry!=0:
            node=ListNode(carry)
            temp.next=node
        return start
        


