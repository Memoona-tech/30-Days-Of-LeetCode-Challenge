# SOLUTION 1 ( Horizontal scanning )
# ------------------ O(n * m) TC ----------- O(1) SC --------

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]  # assume first word is the prefix

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:  # check if prefix matches start
                prefix = prefix[0 : len(prefix) - 1]  # shrink prefix
                if prefix == "":
                    return ""
        return prefix


# SOLUTION 2 ( Vertical scanning )
# ------------------ O(n * m) TC ----------- O(1) SC --------

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):  # check each char of first word
            c = strs[0][i]
            for word in strs[1:]:
                if i == len(word) or word[i] != c:
                    return strs[0][:i]
        return strs[0]


# Solution 3
# ------------------ O(n log (n * m)) TC ----------- O(1) SC --------

  class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""                     # store the final prefix
        v = sorted(v)                # sort words lexicographically (dictionary order)
        first = v[0]                 # first string after sorting
        last = v[-1]                 # last string after sorting

        # only need to compare first and last, since they will differ the most
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:  # if chars differ → stop
                return ans
            ans += first[i]          # otherwise, add char to answer
        return ans

# Solution 4: Divide and Conquer
# ------------------ O(n·m) TC ----------- O(m·log n) SC --------

class Solution:
    def lcp(self, left: str, right: str) -> str:
        i = 0
        while i < len(left) and i < len(right) and left[i] == right[i]:
            i += 1
        return left[:i]

    def helper(self, strs, l, r):
        if l == r:
            return strs[l]
        mid = (l + r) // 2
        left = self.helper(strs, l, mid)
        right = self.helper(strs, mid+1, r)
        return self.lcp(left, right)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return self.helper(strs, 0, len(strs)-1)

