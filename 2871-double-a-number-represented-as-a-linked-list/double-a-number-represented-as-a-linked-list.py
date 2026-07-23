class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        temp = prev
        carry = 0
        last = None
        while temp:
            total = temp.val * 2 + carry
            temp.val = total % 10
            carry = total // 10
            last = temp
            temp = temp.next
        if carry:
            last.next = ListNode(carry)
        curr = prev
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev