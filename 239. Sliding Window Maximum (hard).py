# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # stores indices
        l = r = 0

        while r < len(nums):
            # pop smaller values from queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # if left value is out of bound/window size thne remove it
            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                res.append(nums[q[0]]) # q[0] index has max value
                l += 1
            r += 1
        return res


# SOLUTION 2 --> BRUTE FORCE
# Each max(nums[l:r+1]) takes O(k) 
# ------------------ O(N * K) TC ----------- O(1) SC --------

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        l = 0
        r = k - 1
        res = []
        while r < len(nums):
            res.append(max(nums[l:r+1]))
            l += 1
            r += 1
        return res
