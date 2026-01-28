# SOLUTION 1
# ------------------ O(log n) TC ----------- O(1) SC --------

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]


# SOLUTION 2
# ------------------ O(log n) TC ----------- O(1) SC --------

import bisect

class Solution:
    def searchRange(self, nums, target):
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1

        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]


# SOLUTION 3
# ------------------ O(log n) TC ----------- O(n) SC --------

class Solution:
    def searchRange(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1
        pos = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                pos = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if pos == -1:
            return [-1, -1]

        left = right = pos
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        while right + 1 < n and nums[right + 1] == target:
            right += 1

        return [left, right]

# SOLUTION 4
# ------------------ O(log n) TC ----------- O(1) SC --------

class Solution:
    def searchRange(self, nums, target):
        res = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                if res[0] == -1:
                    res[0] = i
                res[1] = i
        return res
