# Solution 1
# -------------- O(n) TC ------- O(1) SC ----------

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        for i in range(1,len(nums)):
            currSum = max(nums[i], currSum+nums[i])
            maxSum = max(maxSum, currSum)
        return maxSum

# Solution 2
# -------------- O(n) TC ------- O(1) SC ----------
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0
        for i in nums:
            currSum += i
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
        return maxSum


  
        
