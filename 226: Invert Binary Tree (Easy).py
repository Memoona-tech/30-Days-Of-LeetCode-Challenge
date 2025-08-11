# SOLUTION 1
# ------------------ O(no of nodes) TC ----------- O(n) Recursive stack space SC --------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        invert_left = self.invertTree(root.left)
        invert_right = self.invertTree(root.right)
        return node
