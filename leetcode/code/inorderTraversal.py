from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        while root:
            if type(root) is int:
                ans.append(root)
            else:
                if root.right:
                    stack.append(root.right)
                stack.append(root.val)
                if root.left:
                    stack.append(root.left)
            root = stack.pop() if stack else None

        return ans