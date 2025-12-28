# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
            
        suffixMin = [0]*n
        suffixMin[n-1] = nums[n-1]
        
        for i in range(n-2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i+1])
            
        max_score = float('-inf')
        
        for i in range(n-1):
            score = prefix[i] - suffixMin[i+1]
            max_score = max(max_score, score)
        
        return max_score
