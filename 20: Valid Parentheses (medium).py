# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'} 

        for ch in s:
            if ch in mapping:   # it's a closing bracket
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()   # ✅ pop only if it matches
                else:
                    return False  # ❌ mismatch or empty stack
            else:
                stack.append(ch)  # it's an opening bracket
        return not stack


# SOLUTION 2
# ------------------ O(n^2) TC ----------- O(1) SC --------

class Solution:
    def isValid(self, s: str) -> bool:
        prev = None
        while prev != s:
            prev = s
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""


# SOLUTION 3
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
            else:
                count -= 1
                if count < 0:
                    return False
        return count == 0


# SOLUTION 4
# ------------------ O(n^2) TC ----------- O(n) SC --------

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        i = 0
        while i < len(s) - 1:
            if (s[i] + s[i+1]) in ["()", "[]", "{}"]:
                return self.isValid(s[:i] + s[i+2:])
            i += 1
        return False
