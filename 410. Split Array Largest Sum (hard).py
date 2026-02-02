# SOLUTION 1
# ------------------ O(n log(sum(nums))) TC ----------- O(1) SC --------

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def feasible(r):
            pieces = 1
            curr = 0
            for n in nums:
                if curr + n <= r:
                    curr += n
                else:
                    pieces += 1
                    curr = n
            return pieces <= k

        while l <= r:
            mid = (l+r) // 2
            if feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# SOLUTION 2
# ------------------ O(n × sum(nums)) TC ----------- O() SC --------

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(maxSum):
            pieces = 1
            curr = 0
            for n in nums:
                if curr + n <= maxSum:
                    curr += n
                else:
                    pieces += 1
                    curr = n
            return pieces <= k

        left = max(nums)
        right = sum(nums)

        # BRUTE FORCE: try every possible max sum
        for candidate in range(left, right + 1):
            if canSplit(candidate):
                return candidate
