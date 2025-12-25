# SOLUTION 1
# ------------------ O(n log n) TC ----------- O(1) SC --------

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        c = 0
        sm = 0
        l, r = 0, len(people) - 1
        while l <= r:
            sm = people[l] + people[r]
            if sm > limit:
                c += 1
                r -= 1
                sm = 0
            else:
                c += 1
                sm = 0
                l += 1
                r -= 1
        return c

# SOLUTION 2
# ------------------ O(n log n) TC ----------- O(1) SC --------

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        
        return boats
