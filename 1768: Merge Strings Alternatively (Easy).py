# Solution 1 ( not that good)
# -----------------  O((n + m)²) time in the worst case— where n = len(word1) and m = len(word2)  ................. Space: O(n + m) -----------

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i,j in zip(word1, word2):
            res += i+j
        if len(word1)>len(word2):
            for i in range(len(word2), len(word1)):
                res += word1[i]
        else: 
            for j in range(len(word1), len(word2)):
                res += word2[j]
        return res

# TC EXPLANATION BY CHATGPT
#  {
#   In Python each res += ... on an immutable string creates a new string and copies the old contents, so if you do that k times on average you’re copying an average of O(k/2) characters each time.
#}


# Solution 2 (a good one)
# ----------------------------- O(n+m) TC ------------------ Space: O(n + m) (peak)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i,j in zip(word1,word2):
            res += i+j
        if len(word1)>len(word2):
            res += word1[len(word2):]
        if len(word2) > len(word1):
            res += word2[len(word1):]
        return res
