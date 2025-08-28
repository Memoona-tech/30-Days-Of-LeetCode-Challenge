# SOLUTION 1: Pure DFS (Brute Force)
# ------------------ O(2^(m+n)) TC ----------- O(m+n) SC --------
def uniquePaths_dfs(m, n):
    def dfs(i, j):
        # if out of bounds
        if i >= m or j >= n:
            return 0
        # reached destination
        if i == m - 1 and j == n - 1:
            return 1
        return dfs(i + 1, j) + dfs(i, j + 1)
    return dfs(0, 0)


# SOLUTION 2: DFS + Memoization
# ------------------ O(m*n) TC ----------- O(m*n) SC --------
from functools import lru_cache
def uniquePaths_dfs_memo(m, n):
    @lru_cache(None)
    def dfs(i, j):
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        return dfs(i + 1, j) + dfs(i, j + 1)
    return dfs(0, 0)


# SOLUTION 3: Dynamic Programming (Tabulation)
# ------------------ O(m*n) TC ----------- O(m*n) SC --------
def uniquePaths_dp(m, n):
    dp = [[1] * n for _ in range(m)]   # initialize with 1 (first row/col = 1)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]


# SOLUTION 4: Combinatorial Formula
# ------------------ O(min(m, n)) TC ----------- O(1) SC --------
import math
def uniquePaths_math(m, n):
    return math.comb(m+n-2, m-1)   # choose (m-1) downs from (m+n-2) moves


# ------------------ DRIVER CODE ------------------
if __name__ == "__main__":
    m, n = 3, 7
    print("DFS:", uniquePaths_dfs(m, n))
    print("DFS + Memo:", uniquePaths_dfs_memo(m, n))
    print("DP Table:", uniquePaths_dp(m, n))
    print("Combinatorics:", uniquePaths_math(m, n))
