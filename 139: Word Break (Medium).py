# WORD BREAK PROBLEM
# -----------------------------------------------------
# Given a string s and a dictionary of words wordDict,
# return True if s can be segmented into a space-separated
# sequence of one or more dictionary words.


# SOLUTION 1: Dynamic Programming (Bottom-Up)
# ------------------ O(n^2) TC ----------- O(n) SC --------
def wordBreak_dp(s, wordDict):
    n = len(s)
    wordSet = set(wordDict)  # faster lookup
    dp = [False] * (n + 1)
    dp[0] = True  # empty string is valid

    for i in range(1, n + 1):
        for j in range(i):
            # if s[j:i] is in dict and prefix is valid
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[n]
  
# SOLUTION 2: Dynamic Programming (Bottom-Up)
# ------------------ O(n^2) TC ----------- O(n) SC --------

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break
        
        return dp[-1]

# SOLUTION 3: BFS (Queue)
# ------------------ O(n^2) TC ----------- O(n) SC --------
from collections import deque

def wordBreak_bfs(s, wordDict):
    n = len(s)
    wordSet = set(wordDict)
    queue = deque([0])   # start at index 0
    visited = set()

    while queue:
        start = queue.popleft()
        if start in visited:
            continue
        visited.add(start)

        for end in range(start + 1, n + 1):
            if s[start:end] in wordSet:
                if end == n:  # reached the end
                    return True
                queue.append(end)
    return False


# ------------------ DRIVER CODE ------------------
if __name__ == "__main__":
    tests = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("aaaaaaa", ["aaaa", "aaa"], True),
        ("cars", ["car", "ca", "rs"], True),
    ]

    for s, wordDict, expected in tests:
        print(f"s = '{s}', wordDict = {wordDict}")
        print("DP:", wordBreak_dp(s, wordDict))
        print("BFS:", wordBreak_bfs(s, wordDict))
        print(f"Expected: {expected}\n")
