# SOLUTION 1
# ------------------ O(n^3) TC ----------- O(1) SC --------

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        
        for a in range(1, n+1):
            a2 = a*a
            for b in range(1, n+1):
                s = a2 + b*b
                for c in range(1, n+1):
                    if c*c == s:
                        count += 1
        return count

# SOLUTION 2
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0

        max_m = int(math.sqrt(n))+1

        for m in range(2, max_m+1):
            for k in range(1, m):
                
                if (m-k) % 2 == 0:
                    continue
                if math.gcd(m,k) != 1:
                    continue

                a = m*m - k*k
                b = 2*m*k
                c = m*m + k*k

                if c > n:
                    continue

                t = 1
                while t*c <= n:
                    ta, tb, tc = t*a, t*b, t*c
                    if ta <= n and tb <= n:
                        count += 2
                    t += 1
        return count
                



# SOLUTION 3
# ------------------ O(n) TC ----------- O(1) SC --------

import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        # m^2 + k^2 = c  so m up to int(sqrt(n))
        max_m = int(math.sqrt(n)) + 1

        for m in range(2, max_m + 1):
            for k in range(1, m):
                # Enforce primitive triple generation:
                if (m - k) % 2 == 0:
                    # same parity -> skip
                    continue
                if math.gcd(m, k) != 1:
                    # not coprime -> skip
                    continue

                a = m*m - k*k
                b = 2*m*k
                c = m*m + k*k

                if c > n:
                    # even the primitive c is too big; further k (smaller k) might produce larger c?
                    # but we just continue because other k might still be valid
                    continue

                # now count all multiples of this primitive triple
                t = 1
                while True:
                    ta = t * a
                    tb = t * b
                    tc = t * c
                    if tc > n:
                        break
                    # both legs must be <= n
                    if ta <= n and tb <= n:
                        # count both (a,b,c) and (b,a,c)
                        count += 2
                    t += 1

        return count

