# Solution 1 (Brut force) 
# ------------------------------ O(n^2) TC -------------- O(1) SC
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i]+ nums[j] == target:
                        return [i,j]
        return []

# Solution 2 (Fast)
#------------------------------ O(n) TC ------------- but O(n) SC

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]         # and yeah we store value (like 15) as an index & index as a key (means actual value)    e.g. array[15] = 0 , array = [15, 11, 13]
            hashMap[nums[i]] = i        # This is where our hash-map starts building cuz initially it's empty!
        return []
