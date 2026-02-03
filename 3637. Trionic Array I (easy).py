# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

# In this code, i is a pointer to the next element to be processed, not the last processed one.

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        n = len(nums)
        i = 1
        while i < n and nums[i] > nums[i-1]:
            i += 1
        if i == 1 or i == n:
            return False  
        
        while i < n and nums[i] < nums[i-1]:
            i += 1
        if i == n:
            return False

        while i < n and nums[i] > nums[i-1]:
            i += 1
        
        return i == n  
                                                                                                        

# SOLUTION 2
# ------------------ O(n) TC ----------- O(1) SC --------

