# Problem Statement (custom-made for your approach)

# You are given an array people where people[i] represents the weight of the i-th person.
# You are also given an integer limit.
# You have an infinite number of boats.
# Each boat can carry any number of people, as long as the total weight on the boat does not exceed limit.
# People must be boarded in sorted order, and you may fill boats greedily by adding people one by one until the limit is reached or exceeded.
# Once a boat is full (i.e., adding the next person would exceed the limit), you must start a new boat.
# 👉 Return the minimum number of boats needed.


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        boats = 1
        curr_weight = 0
        
        for w in people:
            if curr_weight + w <= limit:
                curr_weight += w
            else:
                boats += 1
                curr_weight = w
        
        return boats


# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC -------- # ❌❌❌❌ FUCKK. IT'S WRONG !!!!!!!

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        count = 0
        i, sm = 0, 0
        j = i+1
        
        while i < n and j < n:
            sm += people[i]   
            def boats(sm):
                if sm == limit:
                    count += 1
                    sm -= people[i]
                    sm -= people[i]
                
                if sm < limit:
                    sm += people[j]
                    self.boats(sm)
                    i += 1
                    j += 1

                if sm > limit:
                    count += 1
                    sm -= people[i]
                
                if sm > limit and j == n-1:
                    count += 1
            
            i += 1
            j += 1
        return count
