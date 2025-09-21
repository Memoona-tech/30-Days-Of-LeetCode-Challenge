from typing import List

# ---------------------------------------------------------
# 1. Brute Force Approach (O(n^3))
# ---------------------------------------------------------
class SolutionBruteForce:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float("inf")
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    curr_sum = nums[i] + nums[j] + nums[k]
                    if abs(curr_sum - target) < abs(closest - target):
                        closest = curr_sum
        return closest


# ---------------------------------------------------------
# 2. Sorting + Two Pointers (Standard O(n^2) solution)
# ---------------------------------------------------------
class SolutionTwoPointers:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")

        for i in range(len(nums) - 2):  # only up to n-3
            l, r = i + 1, len(nums) - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    return curr_sum  # exact match

        return closest


# ---------------------------------------------------------
# 3. Your Enumerate Version (Pythonic O(n^2))
# ---------------------------------------------------------
class SolutionEnumerate:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")

        for i, a in enumerate(nums):
            l, r = i + 1, len(nums) - 1

            while l < r:
                curr_sum = a + nums[l] + nums[r]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    return curr_sum  # exact match

        return closest


# ---------------------------------------------------------
# 4. Optimized Two Pointers with Early Pruning
#    (If sum is already way bigger/smaller than target, skip)
# ---------------------------------------------------------
class SolutionOptimized:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")

        for i in range(len(nums) - 2):
            # Skip duplicates (optional, not necessary but clean)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                # pruning
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    return curr_sum  # exact match

        return closest


# ---------------------------------------------------------
# Example usage (you can test any class here)
# ---------------------------------------------------------
if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1

    print("Brute Force:", SolutionBruteForce().threeSumClosest(nums, target))
    print("Two Pointers:", SolutionTwoPointers().threeSumClosest(nums, target))
    print("Enumerate:", SolutionEnumerate().threeSumClosest(nums, target))
    print("Optimized:", SolutionOptimized().threeSumClosest(nums, target))
