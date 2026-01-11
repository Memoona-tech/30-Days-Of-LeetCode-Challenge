# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        count = 0
        for i, ch in enumerate(s):
            seen.add(ch)
            if len(seen) == (i+1)%3:
                count += 1
        return count

            ©leetcode
