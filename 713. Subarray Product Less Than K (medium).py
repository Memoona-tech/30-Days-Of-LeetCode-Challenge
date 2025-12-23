# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        l, r, pr, c = 0, 0, 1, 0
        n = len(nums)

        while r < n:
            pr *= nums[r]
            while pr >= k:
                pr //= nums[l]
                l += 1
            c += 1 + (r - l)
            r += 1
        return c


# SOLUTION 2
# ------------------ O(n^2) TC ----------- O(1) SC --------

def numSubarrayProductLessThanK(nums, k):
    count = 0
    n = len(nums)
    
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            if prod < k:
                count += 1
            else:
                break
    return count

# SOLUTION 3
# ------------------ O(n log n) TC ----------- O(n) SC --------

import math
import bisect

def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    
    logs = [0]
    for x in nums:
        logs.append(logs[-1] + math.log(x))
    
    logk = math.log(k)
    count = 0
    
    for i in range(len(nums)):
        j = bisect.bisect_left(logs, logs[i] + logk, i + 1)
        count += j - i - 1
    
    return count

