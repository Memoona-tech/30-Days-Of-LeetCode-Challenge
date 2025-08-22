# SOLUTION 1
# ------------------ O(n) TC ----------- O(h) SC --------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root, s):
            if not root:
                return
            s += str(root.val)
            if not root.left and not root.right:                
                res.append(s)
            else:
                s += "->"
                dfs(root.left, s)
                dfs(root.right, s)
        dfs(root, "")
        return res

  # SOLUTION 1
# ------------------ O(n) TC ----------- O(h) SC --------

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []
        stack = [(root, str(root.val))]   # stack holds (node, path_so_far)

        while stack:
            node, path = stack.pop()

            # if leaf node, add path
            if not node.left and not node.right:
                res.append(path)

            # push children with updated paths
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))

        return res

# SOLUTION 1
# ------------------ O(n) TC ----------- O(h) SC --------


from collections import deque

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []
        queue = deque([(root, str(root.val))])

        while queue:
            node, path = queue.popleft()

            if not node.left and not node.right:
                res.append(path)

            if node.left:
                queue.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + "->" + str(node.right.val)))

        return res

