# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[i] = nums[(i + nums[i]) % n]
        return res


# SOLUTION 2
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                res.append(nums[(i+nums[i])%n])
            elif nums[i] < 0:
                val = abs(nums[i])
                res.append(nums[(i+nums[i])%n])
            else:
                res.append(nums[i])
        return res


# SOLUTION 3
# ------------------ O(n) TC ----------- O()1 SC --------

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + nums[i]) % n] for i in range(n)]

# SOLUTION 4
# ------------------ O(n) TC ----------- O()1 SC --------

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i, shift in enumerate(nums):
            res.append(nums[(i + shift) % n])
        return res
