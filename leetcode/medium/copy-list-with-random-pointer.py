from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        res = ""
        cur = self

        while cur:
            res += f" [{cur.val}, {cur.random.val if cur.random else None}]"
            cur = cur.next
        return res


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        copies = {None: None}
        cur = head

        while cur:
            copy = Node(cur.val)
            copies[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = copies[cur]
            copy.next = copies[cur.next]
            copy.random = copies[cur.random]
            cur = cur.next

        return copies[head]



n7 = Node(7)
n13 = Node(13)
n11 = Node(11)
n10 = Node(10)
n1 = Node(1)

n7.next = n13
n13.next = n11
n11.next = n10
n10.next = n1
n1.next = None

n7.random = None
n13.random = n7
n11.random = n1
n10.random = n11
n1.random = n7

Solution().copyRandomList(n7)