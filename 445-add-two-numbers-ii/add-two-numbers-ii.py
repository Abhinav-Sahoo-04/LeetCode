# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(x):
            if x.next is None:
                return x
            prev=None
            temp=x
            while temp!=None:
                next=temp.next
                temp.next=prev
                prev=temp
                temp=next
            return prev
        
        temp=ListNode(0)
        head=temp
        a=reverse(l1)
        b=reverse(l2)
        carry=0
        while a or b:
            val=0
            if a:
                val+=a.val
                a=a.next
            if b:
                val+=b.val
                b=b.next
            val+=carry
            if val>9:
                val%=10
                carry=1
            else:
                carry=0
            temp.next=ListNode(val)
            temp=temp.next
            if carry>0:
                temp.next=ListNode(carry)
        head=head.next
        return reverse(head)
            
            



        