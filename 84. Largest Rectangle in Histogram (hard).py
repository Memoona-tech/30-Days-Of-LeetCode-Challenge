LINK 🔗: [https://youtu.be/Bzat9vgD0fs?si=rN84bE3GGV0HhHf_] --> brute force + optimal

# SOLUTION 1
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


# SOLUTION 2
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
