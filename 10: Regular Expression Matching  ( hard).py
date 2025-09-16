# BEST:  Solution 2

# SOLUTION 1
# ------------------ O(n * m) TC ----------- O(n * m) SC --------

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j>= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j +1) < len(p) and p[j +1] == "*":
                cache[(i, j)] = (dfs(i, j+2) or (match and dfs(i + 1, j)))
                return cache[(i, j)]
            
            if match:
                cache[(i,j)] = dfs(i +1, j+1)
                return cache[(i,j)]
            
            cache[(i,j)] = False
            return False

        return dfs(0, 0)


# Solution 2
# ------------------ O(n * m) TC ----------- O(n * m) SC --------

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True  # empty string matches empty pattern

        for i in range(n, -1, -1):
            for j in range(m - 1, -1, -1):
                match = i < n and (s[i] == p[j] or p[j] == ".")
                if (j + 1) < m and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (match and dp[i + 1][j])
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]

        return dp[0][0]


# Solution 3
# ------------------ O(n * m) TC ----------- O(m) SC --------

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        prev = [False] * (m + 1)
        curr = [False] * (m + 1)
        prev[m] = True  # base case

        for i in range(n, -1, -1):
            curr = [False] * (m + 1)
            for j in range(m - 1, -1, -1):
                match = i < n and (s[i] == p[j] or p[j] == ".")
                if (j + 1) < m and p[j + 1] == "*":
                    curr[j] = prev[j] if match else curr[j + 2]
                    curr[j] = curr[j] or (match and prev[j])
                else:
                    curr[j] = match and prev[j + 1]
            prev = curr

        return prev[0]

