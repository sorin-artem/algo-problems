import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    return helper(tree, float("-inf"), float("inf"))

def helper(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value < min_value or tree.value >= max_value:
        return False
    left_is_valid = helper(tree.left, min_value, tree.value)
    right_is_valid = helper(tree.right, tree.value, max_value)

    return left_is_valid and right_is_valid




root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
print(validateBst(root))
