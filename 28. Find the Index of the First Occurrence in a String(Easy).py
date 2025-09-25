# SOLUTION 1
# ------------------ O(m * n) TC ----------- O(1) SC --------

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m,n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i: i+n] == needle:
                return i
        return -1


# SOLUTION 2
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        # Edge case: empty needle
        if m == 0:
            return 0
        
        r = 0   # pointer for needle
        for i, a in enumerate(haystack):
            if a == needle[r]:
                r += 1
                # if full needle matched
                if r == m:
                    return i - m + 1
            else:
                # reset logic: if mismatch happens
                # but current 'a' could still be start of needle
                if a == needle[0]:
                    r = 1
                else:
                    r = 0
                    
        return -1
