class ListNode:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next

    def __str__(self):
        res = ""
        cur = self

        while cur:
            res += f" [{cur.val}]"
            cur = cur.next
        return res

def generate_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head