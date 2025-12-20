# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        curr_sum = 0
        min_len = float("inf")

        for r in range(len(nums)):
            curr_sum += nums[r]
                
            while curr_sum >= target:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                curr_sum -= nums[l]
                l += 1
        return min_len if min_len != float("inf") else 0  
