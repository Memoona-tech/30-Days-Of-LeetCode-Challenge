# ------------------ O(n) TC ----------- O(1) SC --------
# ✅ BEST SOLUTION (Manual parsing with overflow check)
class Solution1:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 1. Remove leading whitespaces
        if not s:  # if string becomes empty
            return 0

        # 2. Handle sign
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # 3. Parse digits
        num = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # 4. Check overflow before updating num
            if num > (2**31 - 1 - digit) // 10:
                return (2**31 - 1) if sign == 1 else -2**31
            num = num * 10 + digit
            i += 1

        return num * sign


# ------------------ O(n) TC ----------- O(1) SC --------
# Solution 2: Regex-based parsing
import re
class Solution2:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # remove leading spaces
        match = re.match(r'^[\+\-]?\d+', s)  # match sign + digits
        if not match:
            return 0
        num = int(match.group())  # convert matched string to integer
        # clamp to 32-bit range
        return max(min(num, 2**31 - 1), -2**31)


# ------------------ O(n) TC ----------- O(n) SC --------
# Solution 3: String building (simpler but less optimal)
class Solution3:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # remove leading spaces
        if not s:
            return 0

        sign = 1
        i = 0
        if s[0] in ['+', '-']:
            sign = -1 if s[0] == '-' else 1
            i += 1

        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1

        if not num_str:  # no digits found
            return 0

        num = sign * int(num_str)
        return max(min(num, 2**31 - 1), -2**31)
