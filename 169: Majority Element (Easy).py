# BEST SOLUTION: 3

# SOLUTION 1
# ------------------ O(n) TC ----------- O(k) {no. of unique elements in nums} SC --------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)

        for i in count:
            if count[i] > n/2:
                return i

# SOLUTION 2
# ------------------ O(n) TC ----------- O(k) SC --------

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count, key=count.get)


# SOLUTION 3
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
