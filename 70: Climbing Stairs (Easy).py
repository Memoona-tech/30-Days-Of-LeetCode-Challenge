# BEST SOLTUION: 3
# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(n:int) -> int:
            if n==1:
                return 1
            if n==2:
                return 2

            if n in memo:
                return memo[n]
        
            memo[n] = helper(n-1)+helper(n-2)

            return memo[n]
            
        return helper(n)


# SOLUTION 2 (plain recursion without memoization)
# ------------------ O(2^n) TC ----------- O(n) SC --------

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# SOLUTION 3 (iterative with two variables)
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr


# SOLUTION 4 (DP array)
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
