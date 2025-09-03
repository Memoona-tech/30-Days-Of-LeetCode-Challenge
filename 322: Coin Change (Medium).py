# PROBLEM DESCRIPTION
# -------------------
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example:
# Input: coins = [1,2,5], amount = 11
# Output: 3  (because 11 = 5 + 5 + 1)
#
# Constraints:
#   1 <= coins.length <= 12
#   1 <= coins[i] <= 2^31 - 1
#   0 <= amount <= 10^4
#
# Category: Dynamic Programming (Classic DP Problem)
# Approaches: 
#   1. Recursive + Memoization (Top-Down DP)
#   2. Iterative DP (Bottom-Up)
#   3. BFS (Shortest Path Style)

from typing import List


# SOLUTION 1 - RECURSION + MEMOIZATION
# ------------------ O(amount * n) TC ----------- O(amount) SC --------
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(rem):
            if rem == 0: 
                return 0
            if rem < 0: 
                return float("inf")
            ans = float("inf")
            for c in coins:
                ans = min(ans, 1 + dfs(rem - c))
            return ans

        res = dfs(amount)
        return res if res != float("inf") else -1


# SOLUTION 2 - ITERATIVE DP (BOTTOM-UP)
# ------------------ O(amount * n) TC ----------- O(amount) SC --------
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# SOLUTION 3 - BFS APPROACH
# ------------------ O(amount * n) TC ----------- O(amount) SC --------
# Idea: Each state = remaining amount, use BFS to find shortest path to 0
from collections import deque
class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0
        q = deque([(amount, 0)])  # (remaining, steps)
        visited = set([amount])

        while q:
            rem, steps = q.popleft()
            if rem == 0:
                return steps
            for c in coins:
                nxt = rem - c
                if nxt >= 0 and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))
        return -1


# SOLUTION 4 - GREEDY + BACKTRACKING (Not efficient, just for completeness)
# ------------------ Exponential in worst case ----------- O(amount) SC --------
# Tries largest coins first, then backtracks if needed. 
# Only works efficiently for some coin systems (like US coins).
class Solution4:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.ans = float("inf")

        def backtrack(i, rem, count):
            if rem == 0:
                self.ans = min(self.ans, count)
                return
            if i == len(coins): 
                return
            coin = coins[i]
            for k in range(rem // coin, -1, -1):  # try using k coins of this type
                if count + k >= self.ans:  # pruning
                    break
                backtrack(i + 1, rem - k * coin, count + k)

        backtrack(0, amount, 0)
        return self.ans if self.ans != float("inf") else -1
