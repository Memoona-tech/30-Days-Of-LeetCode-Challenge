# SOLUTION 1
# ------------------ O(nlogn + mlogm) TC due to sorting; without sorting it's gonna be O(n + m) but sol won't work! ----------- O(1) SC --------
# Space=O(logn+logm) due to TimSort but Auxiliary space excludes space used by the input and built-in sorting
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        p1, p2 = 0, 0
        count = 0

        while p1 < len(g) and p2 < len(s):
            if g[p1] <= s[p2]:
                p1 += 1
                p2 += 1
                count += 1
            else:
                p2 += 1
        return count
