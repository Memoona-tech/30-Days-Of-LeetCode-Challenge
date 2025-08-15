# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            while res and asteroid < 0 < res[-1]:
                if res[-1] < -asteroid:
                    res.pop()
                    continue
                if res[-1] == -asteroid:
                    res.pop()
                break
            else:
                res.append(asteroid)
        return res

