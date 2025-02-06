from helpers.TreeNode import generate_tree


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


root = generate_tree([4, 2, 7, 1, 3, 6, 9])
print(invertTree(root))
