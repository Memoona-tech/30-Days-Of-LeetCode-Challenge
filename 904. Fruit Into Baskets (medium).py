# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        n = len(fruits)
        freq = {}
        max_len = 0
        for r in range(n):
            freq[fruits[r]] = freq.get(fruits[r], 0) + 1         
            while len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len 
