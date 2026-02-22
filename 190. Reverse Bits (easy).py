# SOLUTION 1
# ------------------ O(32) TC ----------- O(1) SC --------

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1 
        return res
