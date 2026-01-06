# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float('-inf')
        q = deque([root])
        res_level = 1
        curr_level = 1

        while q:
            level_size = len(q)
            level_sum = 0

            for _ in range(level_size):
                node = q.popleft()
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                res_level = curr_level
            
            curr_level += 1
        
        return res_level

# SOLUTION 2
# ------------------ O(n) TC ----------- O(h) / O(n) SC --------

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        levelSum = []

        def dfs(node, level):
            if not node:
                return

            # Ensure list is long enough
            if level == len(levelSum):
                levelSum.append(0)

            levelSum[level] += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        max_sum = float('-inf')
        res_level = 0

        for i in range(len(levelSum)):
            if levelSum[i] > max_sum:
                max_sum = levelSum[i]
                res_level = i

        return res_level + 1  # convert 0-index → 1-index

