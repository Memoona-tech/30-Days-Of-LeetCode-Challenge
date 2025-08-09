# SOLUTION 1
# ------------------ O(n) TC ----------- O(h) SC --------


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:  # Base Case (conditiion 1)
            return None

        if root is p or root is q:  # If current node is p or q   (condition 2)
            return root

        left = self.lowestCommonAncestor(root.left, p, q)         # look into left subtree
        right = self.lowestCommonAncestor(root.right, p, q)       # look into right subtree
        
        if left and right:   # If both sides returned a node, p and q are found in different subtrees → current root is LCA
            return root

        return left if left else right  # If left is not None, return left. Otherwise, return right.

