# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --> only 2 calls in stack --------

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(x):
            if x < 0: 
                return 0
            
            l, curr = 0, 0
            res = 0
            for r in range(len(nums)):
                curr += nums[r]
                while curr > x:
                        curr -= nums[l]
                        l += 1
                res += (r - l + 1)
            return res
        return helper(goal) - helper(goal - 1)
