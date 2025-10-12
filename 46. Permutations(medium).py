# ==========================================================
# 🔢 PROBLEM: Generate all permutations of a given list nums
# ==========================================================

# ==========================================================
# 🧠 APPROACH 1 — Backtracking (In-place Swapping)
# ==========================================================
# ⚙️ Logic:
#   - Fix one position at a time using recursion.
#   - For each position, swap every possible element into it.
#   - Recurse on the next position.
#   - When all positions are filled, store the current list.
#   - Undo (swap back) before moving to the next loop iteration.
#
# 🧩 Example: nums = [1, 2, 3]
#   → [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]
#
# 🕒 Time Complexity: O(N × N!)
#   - There are N! permutations, and each takes O(N) to copy into result.
# 💾 Space Complexity: O(N)
#   - Recursion stack depth = N (ignoring the result storage).
# ==========================================================

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])  # append a copy of current permutation
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # swap
                backtrack(start + 1)  # recurse
                nums[start], nums[i] = nums[i], nums[start]  # backtrack (undo)

        res = []
        backtrack(0)
        return res


# ==========================================================
# 🧠 APPROACH 2 — Backtracking with "Visited Set" + Path
# ==========================================================
# ⚙️ Logic:
#   - Use a separate list (path) to build the current permutation.
#   - Use a "used" set to mark which elements are already taken.
#   - Recursively pick each unused element and continue.
#
# ✅ This avoids modifying the input list and is more intuitive.
#
# 🕒 Time Complexity: O(N × N!)
# 💾 Space Complexity: O(N)
#   - Recursion stack + visited set both take O(N)
# ==========================================================

class Solution2:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path[:])  # add a copy
                return

            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    dfs(path + [nums[i]], used)
                    used.remove(i)

        dfs([], set())
        return res


# ==========================================================
# 🧠 APPROACH 3 — Using Python’s Built-in itertools.permutations
# ==========================================================
# ⚙️ Logic:
#   - The permutations() function from itertools generates
#     all possible arrangements automatically.
#   - It returns tuples; convert them to lists for consistency.
#
# ⚠️ NOTE: Not preferred in interviews — but useful for quick testing.
#
# 🕒 Time Complexity: O(N × N!)
# 💾 Space Complexity: O(N × N!)
#   - Because all permutations are generated and stored at once.
# ==========================================================

from itertools import permutations

class Solution3:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return [list(p) for p in permutations(nums)]
