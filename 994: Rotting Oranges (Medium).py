# ROTTING ORANGES PROBLEM
# -----------------------------------------------------
# You are given an m x n grid where each cell can have one of three values:
#   0 -> empty cell
#   1 -> fresh orange
#   2 -> rotten orange
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange
# becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.

# SOLUTION: Breadth-First Search (BFS)
# ------------------ O(m*n) TC ----------- O(m*n) SC --------
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])

        # Count fresh oranges and push rotten oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # BFS level by level (each level = 1 minute)
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # skip out of bounds and non-fresh cells
                    if (row < 0 or row == rows or col < 0 or col == cols or grid[row][col] != 1):
                        continue
                    # rot the fresh orange
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1


# ------------------ DRIVER CODE ------------------
if __name__ == "__main__":
    tests = [
        ([[2,1,1],[1,1,0],[0,1,1]], 4),
        ([[2,1,1],[0,1,1],[1,0,1]], -1),
        ([[0,2]], 0),
    ]

    solver = Solution()
    for grid, expected in tests:
        print(f"Grid: {grid}")
        print("Output:", solver.orangesRotting(grid))
        print("Expected:", expected)
        print()
