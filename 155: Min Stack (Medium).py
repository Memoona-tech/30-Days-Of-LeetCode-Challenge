# SOLUTION 1
# ------------------ O() TC ----------- O() SC --------

class MinStack:

    def __init__(self):
        self.arr = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.arr:
            val = self.arr.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.arr[-1] if self.arr else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# Solution 2
# NOT THE GOOD ONE DUE TO O(N) OF GET_MIN() AND SOME SPACE ISSUES LIKE OVERRIDING AND WASTES

class MinStack: 

    def __init__(self):
        self.idx = 0
        self.arr = []        

    def push(self, val: int) -> None:
        if self.idx < len(self.arr):
            self.arr[self.idx] = val
        else:
            self.arr.append(val)
        self.idx += 1

    def pop(self) -> None:
        if self.idx > 0:
            self.idx -= 1
            return self.arr[self.idx]
        return None

    def top(self) -> int:
        if self.idx > 0:
            return self.arr[self.idx-1]
        return None

    def getMin(self) -> int:
        if self.idx > 0:
            return min(self.arr[:self.idx])
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


