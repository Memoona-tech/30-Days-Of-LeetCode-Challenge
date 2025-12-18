Fasteest : Solution 2
# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        l = 0
        r = 0

        while l < n and r < n:           
            if s[r] == ' ':
                s[l:r] = reversed(s[l:r])
                l = r+1
            
            if r == n-1:
                s[l:n] = reversed(s[l:n])
            r += 1
            
        return "".join(s)


# SOLUTION 2 (Fastest)
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)

# SOLUTION 3
# ------------------ O() TC ----------- O() SC --------

class Solution:
    def reverseWords(self, s: str) -> str:
        ss = list(s)
        n = len(ss)
        i = 0

        while i < n:
            j = i
            while j < n and ss[j] != " ":
                j += 1

            # reverse characters from i to j-1
            l, r = i, j - 1
            while l < r:
                ss[l], ss[r] = ss[r], ss[l]
                l += 1
                r -= 1

            i = j + 1
        
        return "".join(ss)
