
# SOLUTION 1
# ------------------ O(logn) TC ----------- O(1) SC --------

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n!= 1:
            if n in seen:
                return False
            seen.add(n)

            n = sum(int(d)**2 for d in str(n))
        return n==1

# SOLUTION 1
# ------------------ O(logn) TC ----------- O(1) SC --------

class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNumber(num):
            return sum(int(d)**2 for d in str(num))
        
        slow = n
        fast = nextNumber(n)
        
        while fast != 1 and slow != fast:
            slow = nextNumber(slow)
            fast = nextNumber(nextNumber(fast))
        
        return fast == 1


# SOLUTION 1
# ------------------ O(logn) TC ----------- O(1) SC --------

class Solution:
    def isHappy(self, n: int) -> bool:    
        
        def get_next_number(n):    
            output = 0
            
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            
            return output

        slow = get_next_number(n)
        fast = get_next_number(get_next_number(n))

        while slow != fast:
            if fast == 1: return True
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))

        return slow == 1
v
