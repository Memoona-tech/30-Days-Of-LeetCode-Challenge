# SOLUTION 1
# ------------------ O(n log M) TC ----------- O(1) SC --------
# Time: O(n log M)   where M = max(piles)
# Space: O(1)

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2 # k == mid
            hours = 0

            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

# SOLUTION 2
# ------------------ O(n log M) TC ----------- O(1) SC --------
# Time: O(n log M)   where M = max(piles)
# Space: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed) -> bool:
            # return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower        
            return sum((pile - 1) // speed + 1 for pile in piles) <= h  # faster

        left, right = 1, max(piles)
        while left < right:
            mid = left  + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
