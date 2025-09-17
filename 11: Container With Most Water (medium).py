# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l != r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                r -= 1
        return res

# THE OTHER SOLUTION IS BY USING TWO LOOPS, O( n^2 )
