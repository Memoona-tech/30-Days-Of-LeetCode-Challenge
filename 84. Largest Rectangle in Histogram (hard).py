LINK 🔗: [https://youtu.be/Bzat9vgD0fs?si=rN84bE3GGV0HhHf_] --> brute force + optimal

# Optimal
# SOLUTION 1 + next
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area

# (Canonical Version) Optimal
# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # sentinel

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area



# Brute Force (Check every possible rectangle)
# SOLUTION 2
# ------------------ O(n^2) TC ----------- O(1) SC --------

class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        max_area = 0

        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                area = min_height * (j - i + 1)
                max_area = max(max_area, area)

        return max_area


# Slightly Better Brute Force (Expand left & right per bar)
# SOLUTION 3
# ------------------ O() TC ----------- O() SC --------

class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        res = 0

        for i in range(n):
            l = i
            r = i

            while l >= 0 and heights[l] >= heights[i]:
                l -= 1
            while r < n and heights[r] >= heights[i]:
                r += 1

            width = r - l - 1
            res = max(res, heights[i] * width)

        return res

# SOLUTION 4
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1]*n, [n]*n
        stack = []

        # Nearest Smaller to Left
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Nearest Smaller to Right
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area
