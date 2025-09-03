# PROBLEM DESCRIPTION:
# We are given an m x n grid of heights. Water can flow from a cell to another if 
# the next cell's height <= current cell's height. 
# Pacific ocean touches the left and top border. 
# Atlantic ocean touches the right and bottom border. 
# We need to return coordinates of cells where water can flow to both oceans.

# SOLUTION 1 (DFS from oceans)
# ------------------ O(m*n) TC ----------- O(m*n) SC --------

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        atl, pac = set(), set()
        
        def dfs(r, c, visit, previousHeight):
            if ((r, c) in visit or r == row or c == col or r < 0 or c < 0 or heights[r][c] < previousHeight):
                return
            visit.add((r,c))
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])

        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row - 1, c, atl, heights[row - 1][c])
        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col-1, atl, heights[r][col-1])

        res = []
        for r in range(row):
            for c in range(col):
                if (r, c) in pac and (r, c) in atl: 
                    res.append([r, c])
        return res


# SOLUTION 2 (BFS from oceans)
# ------------------ O(m*n) TC ----------- O(m*n) SC --------

from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])

        def bfs(starts):
            q = deque(starts)
            visit = set(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < row and 0 <= nc < col and 
                        (nr, nc) not in visit and 
                        heights[nr][nc] >= heights[r][c]):
                        visit.add((nr, nc))
                        q.append((nr, nc))
            return visit

        pac_starts = [(0, c) for c in range(col)] + [(r, 0) for r in range(row)]
        atl_starts = [(row-1, c) for c in range(col)] + [(r, col-1) for r in range(row)]

        pac = bfs(pac_starts)
        atl = bfs(atl_starts)

        return list(pac & atl)


# SOLUTION 3 (Multi-source BFS, reverse flow thinking)
# ------------------ O(m*n) TC ----------- O(m*n) SC --------
# Idea: Instead of water flowing to oceans, think of oceans flowing inward.
# Start BFS simultaneously from all Pacific border cells and Atlantic border cells.
# Expand only to neighbors with >= height. Intersection = answer.

from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])

        def bfs_multi(starts):
            q = deque(starts)
            visit = set(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < row and 0 <= nc < col and
                        (nr, nc) not in visit and
                        heights[nr][nc] >= heights[r][c]):
                        visit.add((nr, nc))
                        q.append((nr, nc))
            return visit

        pac_starts = [(0, c) for c in range(col)] + [(r, 0) for r in range(row)]
        atl_starts = [(row-1, c) for c in range(col)] + [(r, col-1) for r in range(row)]

        pac = bfs_multi(pac_starts)
        atl = bfs_multi(atl_starts)

        return list(pac & atl)
