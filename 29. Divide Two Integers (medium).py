# Divide Two Integers Problem Solutions
# -------------------------------------

# Problem:
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator. The integer division should
# truncate toward zero.

# Constraints:
# - -2^31 <= dividend, divisor <= 2^31 - 1
# - divisor != 0

# If result overflows, return INT_MAX (2^31 - 1).



# Solution 1: Bit Manipulation (Efficient Approach)
# ------------- Time Complexity: O(log N), where N = |dividend| ------------ Space Complexity: O(1)

class SolutionBitManipulation:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient

# Solution 2: Repeated Subtraction (Naive Approach)
# ------------- Time Complexity: O(N), where N = |dividend| / |divisor| -------------- # Space Complexity: O(1)

class SolutionNaive:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        return -quotient if negative else quotient


# Solution 3: Using Logarithms (Mathematical Trick)
#----------- Time Complexity: O(1) ------------------------Space Complexity: O(1)------------

# Note: Not recommended for interview unless explicitly allowed,
# because logs and exponentiation internally use multiplication/division.

import math

class SolutionLogarithm:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)
        quotient = int(math.exp(math.log(dividend) - math.log(divisor)))

        return -quotient if negative else quotient

