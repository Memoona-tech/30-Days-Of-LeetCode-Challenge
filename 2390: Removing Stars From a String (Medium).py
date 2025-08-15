# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        string = list(s)
        for i in string:
            if i != '*':
                stack.append(i)                
            else:
                stack.pop()
        return "".join(stack)
