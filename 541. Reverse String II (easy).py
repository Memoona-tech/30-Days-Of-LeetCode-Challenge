# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

# Total blocks ≈ len(ss) / 2k
# work per swap = O(n)
# number of blocks × work per block ≈ (n/2k) ​× k = O(n) 

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        ss = list(s)
        
        for i in range(0,len(ss), 2*k):
            l, r = i, min(i+k-1, len(ss)-1)

            while l < r:
                ss[l], ss[r] = ss[r], ss[l]
                r -= 1
                l += 1

        return "".join(ss)  

# SOLUTION 2
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution(object):
    def reverseStr(self, s, k):
        n = len(s)
        s = list(s)

        for i in range(0, n, 2 * k):
            s[i:i + k] = reversed(s[i:i + k])

        return "".join(s)
