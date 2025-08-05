# ( BEST SOLUTION: 3 )


# Solution 1
# ---------------- O(n) TC ---------- O(n) SC ----------

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_s = s.lower()
        new_s = ""

        for i in lowercase_s:
            if i.isalpha() or i.isdigit():
                new_s += i
        
        if new_s == new_s[::-1]:
            return True
        else:
            return False

# ---------------- O(n) TC ----- O(n) SC ----------

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Filter into a list in one pass
        filtered = [ch.lower() for ch in s if ch.isalnum()]
        # 2. Join once, compare to its reverse
        st = ''.join(filtered)
        return st == st[::-1]

# --------------- O(n) TC -------- O(1) SC ---------

class Solution:
    def isPalindrome(self, s: str) -> bool:
  
        i, j = 0, len(s)-1
        while i < j:
            while i<j and not s[i].isalnum():
                i += 1
            while i<j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
            
        return True


