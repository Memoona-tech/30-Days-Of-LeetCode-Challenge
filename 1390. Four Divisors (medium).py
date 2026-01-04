# SOLUTION 1
# ------------------ O(m · √n) TC ----------- O(1) SC --------
# TC same as below one but practically faster as it stops as count exceed 4 ; also no set operation

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            count = 0
            div_sum = 0

            for i in range(1, int(n**0.5)+1):
                if n % i == 0:
                    j = n // i

                    count += 1
                    div_sum += i

                    if j != i:
                        count += 1
                        div_sum += j
                    
                    if count > 4:
                        break

            if count == 4:
                total += div_sum
                    
        return total


# SOLUTION 2
# ------------------ O( sqrt(n) ) TC ----------- O(1) SC --------

# For the entire list: TC = O(m · √n)
# SC = O(√n)

# While you asked about space, the time complexity is O(N * √M)), where (N) is the number of elements in nums and (M) is the maximum value in nums. 
# This is because for every element in the list, you perform a loop that runs up to the square root of that value.

# Strictly speaking, the space complexity is O(d(n)), where d(n) represents the number of divisors of the value (n). However, in many academic or competitive programming contexts, it is considered O(1) b
# ecause the number of divisors for a standard 32-bit or 64-bit integer is relatively small and bounded by a constant regardless of the length of the input list.

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            divisors = set()
            for i in range(1, int(n**0.5)+1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n//i)
         
            if len(divisors) == 4:
                total += sum(divisors)
                    
        return total
