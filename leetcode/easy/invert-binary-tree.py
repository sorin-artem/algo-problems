from helpers.TreeNode import generate_tree

# stack
def invertTree(root):
    stack = [root]

    while stack:
        cur = stack.pop()
        if not cur:
            continue
        cur.left, cur.right = cur.right, cur.left
        stack.append(cur.left)
        stack.append(cur.right)

    return root

# recursive
def invertTree2(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invertTree2(root.left)
    invertTree2(root.right)

    return root

root = generate_tree([4, 2, 7, 1, 3, 6, 9])
print(invertTree2(root))
