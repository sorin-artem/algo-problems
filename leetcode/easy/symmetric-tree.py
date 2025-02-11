from copy import deepcopy
from inspect import stack
from operator import invert
from turtledemo.penrose import start

from helpers.TreeNode import generate_tree


def isSymetric(root):
    def dfs_compare(left_tree, right_tree):
        if not left_tree and not right_tree:
            return True
        if not left_tree or not right_tree:
            return False

        return left_tree.val == right_tree.val and dfs_compare(left_tree.left, right_tree.right) and dfs_compare(left_tree.right, right_tree.left)

    return dfs_compare(root.left, root.right)


tree = generate_tree([1, 3, 2, 3, 4, 4, 3])
# tree2 = generate_tree([1, 2, 2, None, 3, None, 3])
print(isSymetric(tree))
# print(isSymetric(tree2))
