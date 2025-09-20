# BEST: SOL 1
# SOLUTION 1
# ------------------ O(n^2) TC ----------- O(n) SC --------

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


# SOLUTION 2
# ------------------ O(n^2) TC ----------- O(n) SC --------

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()

        for i in range(n):
            seen = set()
            for j in range(i+1, n):
                target = -nums[i] - nums[j]
                if target in seen:
                    res.add((nums[i], target, nums[j]))
                seen.add(nums[j])
        return [list(r) for r in res]


# SOLUTION 3
# ------------------ O(n^3) TC ----------- O(n) SC --------

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return list(res)

