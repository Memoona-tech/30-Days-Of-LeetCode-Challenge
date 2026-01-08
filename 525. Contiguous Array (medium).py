# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        res = 0
        diff_idx = {}
        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            if n == 1:
                one += 1
            
            if one - zero not in diff_idx:
                diff_idx[one - zero] = i
            
            if one == zero:
                res = one + zero
            else:
                idx = diff_idx[one - zero]
                res = max(res, i - idx)        
        return res
