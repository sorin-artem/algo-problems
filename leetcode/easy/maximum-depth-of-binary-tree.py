# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # stack
    def maxDepth1(self, root) -> int:
        max = 0
        stack = [(root, 1)]
        while stack:
            cur_node, cur_depth = stack.pop()
            if cur_depth > max:
                max = cur_depth
            if cur_node.left:
                stack.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                stack.append((cur_node.right, cur_depth + 1))

        return max

    # recursive
    def maxDepth2(self, root):
        if not root:
            return 0

        return max(self.maxDepth2(root.left) + 1, self.maxDepth2(root.right) + 1)

    # queue
    def maxDepth3(self, root):
        if not root:
            return 0
        queue = [root]
        level = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return level


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.left.left = None
root.left.right = None

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().maxDepth2(root))
