# Zigzag Conversion Problem (LeetCode 6)

# ----------------------------------------------------
# SOLUTION 1 (BEST)  -> Math Indexing
# ------------------ O(n) TC ----------- O(1) SC --------
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        return res

# ----------------------------------------------------
# SOLUTION 2 -> Simulation Row by Row
# ------------------ O(n) TC ----------- O(n) SC --------
class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curRow, step = 0, 1  # start at row 0, moving down

        for ch in s:
            rows[curRow] += ch
            # change direction at the top or bottom
            if curRow == 0:
                step = 1
            elif curRow == numRows - 1:
                step = -1
            curRow += step

        return "".join(rows)


# ----------------------------------------------------
# SOLUTION 3 -> Math Indexing (same as Solution 1 but using list join for efficiency)
# ------------------ O(n) TC ----------- O(n) SC --------
class Solution3:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: 
            return s

        res = []
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res.append(s[i])
                if (r > 0 and r < numRows - 1 
                    and i + increment - 2 * r < len(s)):
                    res.append(s[i + increment - 2 * r])
        return "".join(res)


# ----------------------------------------------------
# Test Run
# ----------------------------------------------------
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3

    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()

    print("Solution 1 (Best - Math Indexing, O(n) TC, O(1) SC):", sol1.convert(s, numRows))
    print("Solution 2 (Simulation, O(n) TC, O(n) SC):          ", sol2.convert(s, numRows))
    print("Solution 3 (Math+Join, O(n) TC, O(n) SC):           ", sol3.convert(s, numRows))
