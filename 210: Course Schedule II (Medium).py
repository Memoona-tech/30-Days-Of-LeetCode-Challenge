# COURSE SCHEDULE II PROBLEM
# -----------------------------------------------------
# Return a possible order to finish all courses given prerequisites.
# Equivalent to finding a topological ordering of a directed graph.
#
# Solutions:
#   1. DFS (topological sort + cycle detection)
#   2. BFS (Kahn's Topological Sort)


# SOLUTION 1: DFS (Topological Sort)
# ------------------ O(V+E) TC ----------- O(V+E) SC --------
from typing import List
from collections import deque

class SolutionDFS:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        res = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:   # cycle detected → invalid
                return False
            if crs in visit:   # already processed
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)   # postorder append
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []      # cycle → no valid ordering

        return res             # already reversed by construction



# SOLUTION 2: BFS (Kahn's Algorithm - Topological Sort)
# ------------------ O(V+E) TC ----------- O(V+E) SC --------
class SolutionBFS:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = {i: [] for i in range(numCourses)}

        # build graph
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []

        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if len(res) == numCourses else []



# ------------------ DRIVER CODE ------------------
if __name__ == "__main__":
    tests = [
        (2, [[1,0]], [[0,1]]),  # valid order: [0,1]
        (4, [[1,0],[2,0],[3,1],[3,2]], [[0,1,2,3],[0,2,1,3]]), # multiple valid
        (2, [[0,1],[1,0]], [[]]) # cycle → []
    ]

    dfs_solver = SolutionDFS()
    bfs_solver = SolutionBFS()

    for numCourses, prereqs, expected in tests:
        print(f"DFS -> {dfs_solver.findOrder(numCourses, prereqs)} (Expected: one of {expected})")
        print(f"BFS -> {bfs_solver.findOrder(numCourses, prereqs)} (Expected: one of {expected})")
        print()
