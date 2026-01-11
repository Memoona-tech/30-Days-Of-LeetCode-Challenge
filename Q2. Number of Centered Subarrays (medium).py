# SOLUTION 1
# ------------------ O(n^2) TC ----------- O(n) SC --------

class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n

        for i in range(n):
            sm = 0
            seen = set()
            for j in range(i, n):
                sm += nums[j]
                seen.add(nums[j])
                if j>i and sm in seen:
                    ans += 1
        return ans    ©leetcode
