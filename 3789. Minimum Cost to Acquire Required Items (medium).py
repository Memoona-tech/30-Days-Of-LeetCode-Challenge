# SOLUTION 1
# ------------------ O(1) TC ----------- O(1) SC --------

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        candidates = [0, need1, need2]
        min_total = float('inf')
        
        for t3 in candidates:
            total = t3 * costBoth + max(0, need1 - t3) * cost1 + max(0, need2 - t3) * cost2
            min_total = min(min_total, total)
        return min_total
