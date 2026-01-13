# ==========================================================
# SOLUTION 1 : Sliding Window with counting even-prefix
# ------------------ O(n) TC ----------- O(1) SC --------
# ==========================================================

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res, odd = 0, 0
        l, m = 0, 0

        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1

            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1
                m = l

            if odd == k:
                while m < len(nums) and nums[m] % 2 == 0:
                    m += 1
                res += (m - l) + 1

        return res


# ==========================================================
# SOLUTION 2 : Prefix Sum + Hash Map
# ------------------ O(n) TC ----------- O(n) SC --------
# ==========================================================

from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        res = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num % 2
            res += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] += 1

        return res


# ==========================================================
# SOLUTION 3 : At Most K Odds Trick
# exactly(k) = atMost(k) - atMost(k-1)
# ------------------ O(n) TC ----------- O(1) SC --------
# ==========================================================

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMost(K):
            l = 0
            odd = 0
            res = 0

            for r in range(len(nums)):
                if nums[r] % 2:
                    odd += 1

                while odd > K:
                    if nums[l] % 2:
                        odd -= 1
                    l += 1

                res += r - l + 1

            return res

        return atMost(k) - atMost(k - 1)
