# BEST SOLUTION: 1
# SOLUTION 1
# ------------------ O(n^2) TC ----------- O(1) SC --------

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for i in range(len(paths)):
            dest = paths[i][1]
            foundAtStart = False

            for j in range(len(paths)):
                if dest == paths[j][0]:
                    foundAtStart = True
                    break
            if not foundAtStart:
                return dest

# SOLUTION 2
# ------------------ O(n^2) TC ----------- O(n) SC --------

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities = {path[0] for path in paths}  # set of all start cities

        for _, end in paths:  # loop through all destination cities
            if end not in start_cities:
                return end
