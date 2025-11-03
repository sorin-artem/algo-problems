from operator import index
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        index_to_remove = length - n
        cur_i = 0
        cur = first
        if index_to_remove == 0:
            return first.next
        while cur_i <= index_to_remove:
            if cur_i == index_to_remove - 1:
                cur.next = cur.next.next
                break
            cur = cur.next
            cur_i += 1

        return first


def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head


list2 = create_list([1, 2, 3, 4])

Solution().removeNthFromEnd(list2, 2)
