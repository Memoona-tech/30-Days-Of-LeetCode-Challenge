# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def subArrayRanges(self, A0):
        res = 0
        inf = float('inf')
        A = [-inf] + A0 + [-inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res -= A[j] * (i - j) * (j - k)
            s.append(i)
            
        A = [inf] + A0 + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res


# SOLUTION 2
# ------------------ O(n^2) TC ----------- O(1) SC --------
    def subArrayRanges(self, A):
        res = 0
        n = len(A)
        for i in xrange(n):
            l,r = A[i],A[i]
            for j in xrange(i, n):
                l = min(l, A[j])
                r = max(r, A[j])
                res += r - l
        return res
