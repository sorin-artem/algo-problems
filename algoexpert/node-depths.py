def nodeDepths(root):
    sum = step(root, 0)

    return sum

def step(root, depth):
    if root is None:
        return 0

    return step(root.left, depth+1) + step(root.right, depth+1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right = BinaryTree(5)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
print(nodeDepths(root))