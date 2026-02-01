# SOLUTION 1
# ------------------ O(N × D) TC ----------- O() SC --------
# N = len(bloomDay)
# D = max(bloomDay) − min(bloomDay)

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Quick impossible check
        if m * k > len(bloomDay):
            return -1

        min_day = min(bloomDay)
        max_day = max(bloomDay)

        # Try every day
        for day in range(min_day, max_day + 1):
            bouquets = 0
            flowers = 0

            for d in bloomDay:
                if d <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                return day

        return -1

# SOLUTION 2
# ------------------ O(n log D) TC ----------- O(1) SC --------
# n = number of flowers
# D = range of days

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Impossible case
        if m * k > len(bloomDay):
            return -1

        l, r = min(bloomDay), max(bloomDay)
        res = -1

        def feasible(day):
            bouquets = 0
            flowers = 0

            for d in bloomDay:
                if d <= day:          # flower has bloomed
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0       # break consecutive streak

            return bouquets >= m

        while l <= r:
            mid = (l + r) // 2
            if feasible(mid):
                res = mid            # possible answer
                r = mid - 1          # try smaller day
            else:
                l = mid + 1          # need more days

        return res
