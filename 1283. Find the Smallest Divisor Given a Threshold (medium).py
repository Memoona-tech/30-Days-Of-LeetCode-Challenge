# SOLUTION 1
# ------------------ O(N × max(nums)) TC ----------- O(1) SC --------

import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_val = max(nums)

        for d in range(1, max_val + 1):
            total = 0
            for n in nums:
                total += math.ceil(n / d)

            if total <= threshold:
                return d

# SOLUTION 2
# ------------------ O(N × max(nums)) TC ----------- O() SC --------

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        for d in range(1, max(nums) + 1):
            total = 0
            for n in nums:
                total += (n - 1) // d + 1

            if total <= threshold:
                return d


# SOLUTION 3
# ------------------ O(N × log(max(nums))) TC ----------- O(1) SC --------

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        res = r
        sums = 0

        while l <= r:
            d = (l+r) // 2

            for n in nums:
                sums += ceil(n/d)

            if sums <= threshold:
                res = min(d, res)
                r = d - 1
            else:
                l = d + 1
                
            sums = 0
        return res
