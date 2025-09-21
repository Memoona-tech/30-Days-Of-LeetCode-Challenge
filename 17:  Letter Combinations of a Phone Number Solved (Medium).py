# SOLUTION 1
# ------------------ O(n * 4^n) TC ----------- O(n) SC --------

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',   
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i+1, curStr + c)
        if digits:
            backtrack(0, "")
        return res

# SOLUTION 2
# ------------------ O(n * 4^n) TC ----------- O(1) SC --------

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',   
        }

        res = [""]
        for d in digits:
            temp = []
            for prefix in res:
                for c in digitToChar[d]:
                    temp.append(prefix + c)
            res = temp
        return res


# SOLUTION 1
# ------------------ O(n * 4^n) TC ----------- O(n * 4^n) SC --------

import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',   
        }
        groups = [digitToChar[d] for d in digits]
        return ["".join(p) for p in itertools.product(*groups)]

