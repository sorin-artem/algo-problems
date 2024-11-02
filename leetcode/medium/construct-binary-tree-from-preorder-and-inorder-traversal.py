# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def buildTree(preorder, inorder ):
#     print(preorder)
#     if not preorder or not inorder:
#         return None
#     root_value = preorder.pop(0)
#     idx = inorder.index(root_value)
#     root_node = TreeNode(root_value)
#     root_node.left = buildTree(preorder, inorder[:idx])
#     root_node.right = buildTree(preorder, inorder[idx+1:])
#     return root_node

def buildTree(preorder, inorder ):
    hash_map = {}

    for i in range(len(inorder)):
        hash_map[inorder[i]] = i
    print(hash_map)
    def helper(left, right):
        if left>right:
            return None
        root_value = preorder.pop(0)
        mid = hash_map[root_value]
        root = TreeNode(root_value)

        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)

        return root

    return helper(0, len(inorder) - 1)


print(buildTree([3,9,20,15,7], [9,3,15,20,7]))
