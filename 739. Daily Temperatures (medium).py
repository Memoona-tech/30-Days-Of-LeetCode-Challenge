# SOLUTION 1
# ------------------ O(n^2) TC ----------- O(1) SC --------

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        for i in range(n):
            cur = temperatures[i]
            j = i + 1
            c = 0
            while j < n and cur >= temperatures[j]:
                c += 1   
                j += 1            
            if j < n:
                c += 1
                answer[i] = c
        return answer

# SOLUTION 2
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        i = 0
        for i in range(n):
            cur = temperatures[i]
            while stack and cur > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer  
