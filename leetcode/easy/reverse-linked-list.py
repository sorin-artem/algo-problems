from typing import Optional

from helpers import ListNode
from helpers.ListNode import generate_linked_list

# Example usage
values = generate_linked_list([1, 2, 3, 4, 5])


def reverse(head: Optional[ListNode]):
    prev, cur = None, head

    while cur:
        saved_next = cur.next
        cur.next = prev
        prev = cur
        cur = saved_next

    return prev


print(reverse(values))
