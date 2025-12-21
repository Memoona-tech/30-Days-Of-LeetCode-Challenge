# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, mid = 0, 0
        hi = len(nums) - 1
        
        while mid <= hi:
            if  nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
        return nums  

# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = count1 = count2 = 0

        # 1st pass: count
        for x in nums:
            if x == 0:
                count0 += 1
            elif x == 1:
                count1 += 1
            else:
                count2 += 1

        # 2nd pass: overwrite
        i = 0
        for _ in range(count0):
            nums[i] = 0
            i += 1
        for _ in range(count1):
            nums[i] = 1
            i += 1
        for _ in range(count2):
            nums[i] = 2
            i += 1
