class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    res = ListNode()
    current = res
    carry = 0
    while l1 or l2:
        n1 = l1.val if l1 else 0
        n2 = l2.val if l2 else 0
        new_number = n1 + n2 + carry
        carry = 1 if new_number >= 10 else 0
        new_digit = new_number % 10
        current.next = ListNode(new_digit)

        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
        current = current.next

    if carry:
        current.next = ListNode(1)

    return res.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(9)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)

# l1 = ListNode(9)
# l1.next = ListNode(9)
# l1.next.next = ListNode(9)
# l1.next.next.next = ListNode(9)
# l1.next.next.next.next  = ListNode(9)
# l1.next.next.next.next.next   = ListNode(9)
# l1.next.next.next.next.next.next    = ListNode(9)
# #
# l2 = ListNode(9)
# l2.next = ListNode(9)
# l2.next.next = ListNode(9)
# l2.next.next.next = ListNode(9)
print(addTwoNumbers(l1, l2))
