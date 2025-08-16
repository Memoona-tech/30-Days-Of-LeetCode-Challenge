# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = Counter(s)

        total = 0
        odd_found = False
        for i in frequency:
            if frequency[i]%2 == 0:
                total += frequency[i]
            else:
                total += frequency[i] - 1
                odd_found = True
        if odd_found:
            total += 1
        return total

