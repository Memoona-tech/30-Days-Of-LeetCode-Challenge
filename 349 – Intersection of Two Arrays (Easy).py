# SOLUTION 1
# ------------- O(n + m) TC ------------- O(n + m) SC -----------

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = list(set(nums1) & set(nums2))
        return intersection

# SOLUTION 2
# ------------- O(n + m) TC ------------- O(min(n + m)) SC

a = [1, 2, 3 ,8 ,7 ,80]
b = [1, 40, 8, 2, 10]

res = [ value for values in a if value in b ]
    return res
