# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    empty = ListNode()
    tail = empty
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2.val
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    return tail

print(mergeTwoLists([1, 2, 4], [1, 3, 4]))
