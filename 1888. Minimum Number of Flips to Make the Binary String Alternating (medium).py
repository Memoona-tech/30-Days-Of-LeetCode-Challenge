# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        
        # Create the two target alternating patterns of length 2n
        target1 = ""  # starting with '0'
        target2 = ""  # starting with '1'
        for i in range(2 * n):
            target1 += '0' if i % 2 == 0 else '1'
            target2 += '1' if i % 2 == 0 else '0'
        
        diff1 = 0  # differences with target1
        diff2 = 0  # differences with target2
        result = n
        
        # Sliding window of length n
        for i in range(2 * n):
            # Add the new character to the window
            if s[i] != target1[i]:
                diff1 += 1
            if s[i] != target2[i]:
                diff2 += 1
            
            # If window size exceeds n, remove the leftmost character
            if i >= n:
                if s[i - n] != target1[i - n]:
                    diff1 -= 1
                if s[i - n] != target2[i - n]:
                    diff2 -= 1
            
            # If we have a complete window of size n, update result
            if i >= n - 1:
                result = min(result, diff1, diff2)
        
        return result
