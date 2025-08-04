# --------------- O(n) TC ----------- O(1) SC -------------

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZero = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[nonZero], nums[curr] = nums[curr], nums[nonZero]     # O(1)
                nonZero += 1
