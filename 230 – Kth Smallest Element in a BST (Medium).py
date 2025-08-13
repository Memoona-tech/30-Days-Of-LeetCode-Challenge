# BEST SOLUTION: 2
# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        k -= 1
        def inOrder(node):
            if not node:
                return 
            inOrder(node.left)
            arr.append(node.val)
            inOrder(node.right)
        inOrder(root)
        return arr[k]

# SOLUTION 2
# ------------------ O(k + h) TC ----------- O(h) SC --------

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None
        
        def inOrder(node):
            if not node:
                return
            
            inOrder(node.left)
            
            self.count += 1
            if self.count == k:
                self.result = node.val
                return  # Found the k-th smallest, stop
            
            inOrder(node.right)
        
        inOrder(root)
        return self.result
