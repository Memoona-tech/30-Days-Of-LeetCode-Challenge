# COURSE SCHEDULE PROBLEM
# -----------------------------------------------------
# Determine if you can finish all courses given prerequisites.
# Equivalent to checking if the directed graph has a cycle.
#
# Solutions:
#   1. DFS (cycle detection with recursion)
#   2. BFS (Kahn's Topological Sort)


# SOLUTION 1: DFS (Cycle Detection)
# ------------------ O(V+E) TC ----------- O(V+E) SC --------
from typing import List

class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()  # tracks current recursion path

        def dfs(crs):
            if crs in visitSet:   # cycle detected
                return False
            if preMap[crs] == []: # no prereqs
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            visitSet.remove(crs)
            preMap[crs] = []      # memoize as finished
            return True

        for crs in range(numCourses):
            if not dfs(crs): 
                return False
        return True



# SOLUTION 2: BFS (Kahn's Algorithm)
# ------------------ O(V+E) TC ----------- O(V+E) SC --------
from collections import deque

class SolutionBFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = {i: [] for i in range(numCourses)}

        # build graph
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0

        while q:
            node = q.popleft()
            taken += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return taken == numCourses



# ------------------ DRIVER CODE ------------------
if __name__ == "__main__":
    tests = [
        (2, [[1,0]], True),
        (2, [[1,0],[0,1]], False),
        (4, [[1,0],[2,1],[3,2]], True),
    ]

    dfs_solver = SolutionDFS()
    bfs_solver = SolutionBFS()

    for numCourses, prereqs, expected in tests:
        print(f"DFS -> {dfs_solver.canFinish(numCourses, prereqs)} (Expected: {expected})")
        print(f"BFS -> {bfs_solver.canFinish(numCourses, prereqs)} (Expected: {expected})")
        print()
