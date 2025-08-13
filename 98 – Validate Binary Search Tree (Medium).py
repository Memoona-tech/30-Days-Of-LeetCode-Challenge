# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            if not node:
                return True
            
            if not(low < node.val < high):  # the opposite one will not work cuz it will immediately return True even if it just checked the current one.
                                            # but here we only return anything(False) when it's False(not in bounds) cuz we don't need to proceede cuz we know it's(BST) is voilating
                return False
            return (helper(node.left, low, node.val) and helper(node.right, node.val, high))
        
        return helper(root, float('-inf'), float('inf'))
