# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        res = ListNode()
        start = res

        while cur1 or cur2:
            if cur1 and (cur2 is None or cur1.val < cur2.val):
                res.next = cur1
                res = res.next
                cur1 = cur1.next
                continue
            if cur2 and (cur1 is None or cur2.val <= cur1.val):
                res.next = cur2
                res = res.next
                cur2 = cur2.next
                continue

        return start.next


# Helper function to create linked list from array
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

# Helper function to print linked list


def print_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))


# Test case: [1,2,4] and [1,3,5]
list1 = create_list([1, 2, 4])
list2 = create_list([1, 3, 5])

print("List 1:", end=" ")
print_list(list1)
print("List 2:", end=" ")
print_list(list2)

result = Solution().mergeTwoLists(list1, list2)
print("Merged:", end=" ")
print_list(result)
