# MOSTLY USED: solution 2 cuz You don’t have to carry an extra currentSum and also the original target.
# SOLUTION 1
# ------------------ O(n) TC ----------- O(h) SC --------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findSum(root, targetSum):
            if not root:
                return False

            if not root.left and not root.right:
                return targetSum == root.val

            targetSum -= root.val 
            
            return  findSum(root.left, targetSum) or findSum(root.right, targetSum)
        return findSum(root, targetSum)

# SOLUTION 1
# ------------------ O(n) TC ----------- O(h) SC --------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def findSum(root, currSum):
            if not root:
                return False

            currSum += root.val 

            if not root.left and not root.right:
                return currSum == targetSum            

            return  findSum(root.left, currSum) or findSum(root.right, currSum)
        return findSum(root, 0)
