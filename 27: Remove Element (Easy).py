# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # pointer for the next valid position
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# SOLUTION 2
# ------------------ O(n) TC ----------- O(1) SC --------

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]   
            k += 1
    return k


