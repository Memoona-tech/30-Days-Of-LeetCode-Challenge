# SOLUTION 1
# ------------------ O(nlogn) TC ----------- O(1) SC --------

class Solution:
    def minimumDifference(self, nums, k):
        if k <= 1:
            return 0

        nums.sort()
        ans = float('inf')

        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])

        return ans

# SOLUTION 2
# ------------------ O(nlogn) TC ----------- O(1) SC --------

class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        ans = float('inf')
        l, r = 0, k - 1

        while r < len(nums):
            ans = min(ans, nums[r] - nums[l]) 
            l, r = l+1, r + 1

        return ans
