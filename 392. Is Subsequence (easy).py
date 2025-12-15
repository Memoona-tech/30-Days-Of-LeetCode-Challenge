# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if t == "":
            return False

        s1, t1 = 0, 0

        while s1 < len(s) and t1 < len(t):
            if s[s1] == t[t1]:
                s1 += 1
                t1 += 1
            else:
                t1 += 1
        if s1 == len(s):
            return True
        return False
