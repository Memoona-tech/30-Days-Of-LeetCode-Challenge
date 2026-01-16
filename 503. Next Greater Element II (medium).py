# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def nextGreaterElements(self, A):
        n = len(A)
        stack, res = [], [-1] * n
        for i in range(2 * n):                         # loop twice, through array
            while stack and (A[stack[-1]] < A[i%n]):
                res[stack.pop()] = A[i%n]
            if i < n:
                stack.append(i)
        return res

#OR -- if above don't work

class Solution(object):
    def nextGreaterElements(self, nums):
        stack, res = [], [-1] * len(nums)
        for i in range(len(nums)):
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res


# SOLUTION 2  (Brute Force (for learning only))
# ------------------ O(n^2) TC ----------- O(1) SC --------

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n

        for i in range(n):
            for j in range(1, n):
                if nums[(i + j) % n] > nums[i]:
                    res[i] = nums[(i + j) % n]
                    break
        return res


# SOLUTION 3  (Using values instead of indices (less common))
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if i < n:
                res[i] = stack[-1] if stack else -1
            stack.append(nums[i % n])

        return res

