from typing import List, Optional

from helpers.TreeNode import TreeNode


# time: O(n2)
class Solution2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        index = inorder.index(root.val)
        root.right = self.buildTree(inorder[index + 1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)

        return root


# time: O(n)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapping = {}
        for i in range(len(inorder)):
            mapping[inorder[i]] = i

        def build(left, right):
            if left > right:
                return None

            root = TreeNode(postorder.pop())
            index = mapping[root.val]
            root.right = build(index + 1, right)
            root.left = build(left, index - 1)
            return root

        return build(0, len(postorder) - 1)

s = Solution()
print(s.buildTree([9,3,15,20,7], [9,15,7,20,3]))