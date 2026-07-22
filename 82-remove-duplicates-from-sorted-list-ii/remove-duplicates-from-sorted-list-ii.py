# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        frq=[]
        temp=head
        while temp:
            frq.append(temp.val)
            temp=temp.next
        d={}
        for i in frq:
            d[i]=frq.count(i)
        print(d)
        temp=head.next
        prev=head
        while temp:
            if d[temp.val] > 1:
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        if d[head.val]>1:
            head=head.next
        return head
        
            

                
