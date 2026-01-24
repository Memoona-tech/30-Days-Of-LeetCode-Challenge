# SOLUTION 1
# ------------------ O(nlogn) TC ----------- O(1) SC --------

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n-1
        res = 0
        while l < r:
            sums = nums[l]+nums[r]
            res = max(res, sums)
            l += 1
            r -= 1
        return res 
