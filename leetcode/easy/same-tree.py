from helpers.TreeNode import list_to_tree
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isSameTree(p, q):
    if p and not q:
        return False
    if q and not p:
        return False
    if q and p and q.val != p.val:
        return False

    if not q and not p:
        return True

    return isSameTree(q.left, p.left) and isSameTree(q.right, p.right)



p = list_to_tree([1, 2, 3, 6])
q = list_to_tree([1, 2, 3, 6])

print(isSameTree(p, q))
