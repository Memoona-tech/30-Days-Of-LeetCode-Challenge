# SOLUTION 1
# ------------------ O(log n) TC ----------- O(log n) SC --------

class Solution:
    def binarySearch(self, nums, target, left, right) -> int:

        if left > right:
            return left
            
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif target > nums[mid]:
            return self.binarySearch(nums, target, mid + 1, right)

        else:
            return self.binarySearch(nums, target, left, mid - 1)
            
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)   


# SOLUTION 2
# ------------------ O(log n) TC ----------- O(1) SC --------

class Solution:
    def binarySearch(self, nums, target, left, right) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                left = mid + 1

            else:
                right = mid - 1
        
        return left 
            
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)   

    
