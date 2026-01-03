# SOLUTION 1 (Brute Force)
# ------------------ O(n^2 + m) TC ----------- O(m) SC --------

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        res, resLen = [-1, -1], float("inf")

        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = countS.get(s[j], 0) + 1

                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break

                if flag and (j-i+1) < resLen:
                    resLen = j-i+1
                    res = [i, j]
                    
        l, r = res
        return s[l: r+1] if resLen != float("inf") else ""


# SOLUTION 2 (Sliding window)
# ------------------ O(n+m) TC ----------- O(m) SC --------

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l: r+1] if resLen != float("inf") else ""
