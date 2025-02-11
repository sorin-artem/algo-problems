from typing import List

from helpers.TreeNode import TreeNode


# O(n^2) time
def buildTree1(self, preorder: List[int], inorder: List[int]):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree1(preorder[1:mid + 1], inorder[:mid])
    root.right = buildTree1(preorder[mid + 1:], inorder[mid + 1:])

    return root


# O(n) time
def buildTree(preorder: List[int], inorder: List[int]):
    mapping = {}
    for i in range(len(inorder)):
        mapping[inorder[i]] = i

    def build(start, end):
        if start > end:
            return None
        root = TreeNode(preorder.pop(0))
        mid = mapping[root.val]
        root.left = build(start, mid - 1)
        root.right = build(mid + 1, end)

    return build(0, len(preorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
buildTree(preorder, inorder)
