# SOLUTION 1
# ------------------ O(n+m) TC ----------- O(n+m) SC --------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def Serialize(node):
            if not node:
                return "N"
            return f"({node.val},{Serialize(node.left)},{Serialize(node.right)})"
        
        rootSerialize = Serialize(root)
        subRootSerliaze = Serialize(subRoot)
        return subRootSerliaze in rootSerialize

# SOLUTION 1
# ------------------ O(n+m) TC ----------- O(h1+h2) SC --------

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def helper(p, q):
            if not p:
                return False
            if isSameTree(p, q):
                return True
            return helper(p.left, q) or helper(p.right, q)

        return helper(root, subRoot)
