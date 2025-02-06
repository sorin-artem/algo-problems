class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"val={self.val}, left={self.left}, right={self.right}"

def generate_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    nodes = [root]
    i = 1
    while i < len(lst):
        node = nodes.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            nodes.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            nodes.append(node.right)
        i += 1
    return root