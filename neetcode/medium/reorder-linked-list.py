from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev
        first = head
        while second:
            temp1 = first.next 
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            



def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head


list2 = create_list([0, 1, 2, 3, 4, 5, 6])

Solution().reorderList(list2)
