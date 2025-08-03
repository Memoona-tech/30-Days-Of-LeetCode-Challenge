#  Solution 1 (General)
# ------------------------------ O(n) TC --------- O(1) SC -----------------
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# Solution 2 (fast) + hash set
# --------------------------- O(n) avg TC ---------- O(n) SC ----------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        n = len(nums)

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


# Solution 3 (using sorting)
# -------------------------- O(n log(n)) TC ------------ O(1) SC --------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


# Solution 4 ----------- using hash-map
# --------------------------- O(n) TC ------------- O(n) SC --------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:      # num in seen tells you “have I ever seen this number before?”
                return True                         # seen[num] >= 1 tells you “and have I seen it at least once already?”
                                                    # Together, they detect the second (or later) time you hit the same value—i.e. a duplicate—so you can immediately return True.                
          
            seen[num] = seen.get(num, 0) + 1        # seen.get(num, 0) fetches the current count (or 0 if it’s the first time).
                                                    # You then increment by one, so that the next time you see num, seen[num] will be ≥ 1.
        return False






