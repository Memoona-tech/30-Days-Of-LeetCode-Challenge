# SOLUTION 1
# ------------------ O(log₁₀(n)) TC ----------- O(1) SC --------
# TC = O(log₁₀(n)) ≈ O(d) where d = number of digits

class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 1 else 1
        x = abs(x)
        res = 0
        
        while x != 0:
            digit = x % 10
            res = res * 10 + digit
            x = x // 10
        res *= sign

        if res < -2 **31 or res > 2**31 - 1:
            return 0
        return res


# SOLUTION 2
# ------------------ O(d) TC ----------- O(d) SC --------
# SC = O(d) because of recursion stack frames (one per digit)
# Recursive Solution (just for learning, not common)
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        def helper(x, res=0):
            if x == 0:
                return res
            digit = x % 10
            return helper(x // 10, res * 10 + digit)

        res = helper(x) * sign

        # 32-bit signed integer check
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

  
