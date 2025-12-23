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
