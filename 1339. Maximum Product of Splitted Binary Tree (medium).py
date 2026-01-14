#  BEST - 2nd solution BUT FAST - 1st

# ============================================================
# SOLUTION 1: DFS + Store All Subtree Sums
# ------------------ O(n) TC ----------- O(n) SC --------------
#
# Idea:
#   - DFS to compute sum of every subtree
#   - Store each subtree sum in a list
#   - Try all possible splits: s * (total - s)
#
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        sums = []

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            s = left + right + node.val
            sums.append(s)
            return s

        total = dfs(root)
        res = 0
        for s in sums:
            res = max(res, s * (total - s))
        return res % MOD

# ============================================================
# SOLUTION 2: Two-Pass DFS (Optimal, No Extra List)
# ------------------ O(n) TC ----------- O(h) SC --------------
#
# Idea:
#   - First DFS: compute total tree sum
#   - Second DFS: compute subtree sums and update max product
#
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.res = max(self.res, s * (total - s))
            return s

        dfs(root)
        return self.res % MOD


# ============================================================
# SOLUTION 3: Single DFS + Pythonic max()
# ------------------ O(n) TC ----------- O(n) SC --------------
#
# Idea:
#   - Same as Solution 1
#   - Use Python's max() for cleaner computation
#
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        subs = []

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            subs.append(s)
            return s

        total = dfs(root)
        return max(s * (total - s) for s in subs) % MOD


# ============================================================
# SOLUTION 4: Iterative Postorder DFS (No Recursion)
# ------------------ O(n) TC ----------- O(n) SC --------------
#
# Idea:
#   - Simulate postorder traversal using stack
#   - Store subtree sums in a hashmap
#
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        stack = [(root, False)]
        subtree = {}
        total = 0

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                left = subtree.get(node.left, 0)
                right = subtree.get(node.right, 0)
                subtree[node] = node.val + left + right
                total += node.val
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        res = 0
        for s in subtree.values():
            res = max(res, s * (total - s))
        return res % MOD
