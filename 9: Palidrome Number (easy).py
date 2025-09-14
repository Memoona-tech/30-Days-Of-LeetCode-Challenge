"""
Palindrome Number Problem (LeetCode #9)

We check if an integer is a palindrome (reads the same forward and backward).
Best solution = Solution 4 (reverse only half of the number).
"""

# ✅ SOLUTION 4 (Most Optimized: Reverse Half)
# ------------------ O(log x) TC ----------- O(1) SC --------
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse = 0
        while x > reverse:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        return x == reverse or x == reverse // 10


# SOLUTION 3 (Reverse Full + Early Checks)
# ------------------ O(log x) TC ----------- O(1) SC --------
class Solution3:
    def isPalindrome(self, x: int) -> bool:
        xcopy = x
        reverse = 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        return xcopy == reverse


# SOLUTION 1 (Basic Full Reverse)
# ------------------ O(log x) TC ----------- O(1) SC --------
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        xcopy = x
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        return reverse == xcopy


# SOLUTION 2 (String Approach)
# ------------------ O(n) TC ----------- O(n) SC --------
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        str2 = str1[::-1]
        return str1 == str2


# ------------------ TESTING ------------------
if __name__ == "__main__":
    nums = [121, -121, 10, 12321, 1221, 0]
    solver = Solution()   # ✅ Best solution
    for n in nums:
        print(f"{n} -> {solver.isPalindrome(n)}")
