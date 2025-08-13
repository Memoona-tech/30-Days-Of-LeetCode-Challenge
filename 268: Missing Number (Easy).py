# BEST SOLUTION: 1, 2
# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    total_sum = (n * (n+1)) //2
    nums_sum = 0

    nums_sum = sum(nums)  

    return total_sum - nums_sum

{
arr = | 3 | 0 | 1 |

size of nums = 3

Sum of n numbers = n(n+1)/2

(1+2+3)

sum of nums = 4

(3+0+1)

ans = num of n numbers - sum of nums vector.

ans = 6 - 4 = 2
}


# SOLUTION 2
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
      
# SOLUTION 3
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        v = [-1] * (n + 1)
        for num in nums:
            v[num] = num
        for i in range(len(v)):
            if v[i] == -1:
                return i
        return 0

