# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------
# ( explanation by Apna Clg )
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to produce the next lexicographical permutation.
        """

        # Step 1: Find the first index i such that nums[i] < nums[i+1], scanning from right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If such i exists, find rightmost element greater than nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the part after i to get the smallest possible suffix
        nums[i + 1:] = reversed(nums[i + 1:])
