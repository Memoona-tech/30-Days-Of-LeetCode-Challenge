# SOLUTION 1
# ------------------ O(log n) TC ----------- O(1) SC --------

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 0
        def mask(n):
            m = 1
            while m <= n:
                m *= 2
            return m
        return n^(mask(n)-1)
        
