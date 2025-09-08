# BEST & MOST USED: SOL 2 & 5
# LeetCode 3: Longest Substring Without Repeating Characters

# SOLUTION 1: Sliding Window with Set (your solution)
# ------------------ O(n) TC ----------- O(n) SC --------
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


# SOLUTION 2: Sliding Window with HashMap (store last index)
# ------------------ O(n) TC ----------- O(n) SC --------
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndex = {}
        l, res = 0, 0
        for r, ch in enumerate(s):
            if ch in charIndex and charIndex[ch] >= l:
                l = charIndex[ch] + 1  # jump left pointer
            charIndex[ch] = r
            res = max(res, r - l + 1)
        return res


# SOLUTION 3: Brute Force (Check all substrings)
# ------------------ O(n^3) TC ----------- O(min(n, charset)) SC --------
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def allUnique(sub):
            return len(set(sub)) == len(sub)
        n, res = len(s), 0
        for i in range(n):
            for j in range(i+1, n+1):
                if allUnique(s[i:j]):
                    res = max(res, j - i)
        return res


# SOLUTION 4: Optimized Brute Force with HashSet
# ------------------ O(n^2) TC ----------- O(n) SC --------
class Solution4:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, res = len(s), 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                res = max(res, j - i + 1)
        return res


# SOLUTION 5: Sliding Window with ASCII Array
# ------------------ O(n) TC ----------- O(1) SC --------
class Solution5:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = [-1] * 128   # ASCII characters
        l, res = 0, 0
        for r, ch in enumerate(s):
            l = max(l, index[ord(ch)] + 1)
            index[ord(ch)] = r
            res = max(res, r - l + 1)
        return res
