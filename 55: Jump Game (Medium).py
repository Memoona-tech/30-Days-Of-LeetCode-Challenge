# JUMP GAME PROBLEM
# -----------------------------------
# You are given an integer array nums. Each element represents
# your maximum jump length at that position. Return True if you
# can reach the last index, otherwise False.


# SOLUTION 1: Brute Force (DFS)
# ------------------ O(2^n) TC ----------- O(n) SC (stack depth) --------
def canJump_dfs(nums):
    n = len(nums)

    def dfs(position):
        if position == n - 1:
            return True
        furthest_jump = min(position + nums[position], n - 1)
        for next_pos in range(position + 1, furthest_jump + 1):
            if dfs(next_pos):
                return True
        return False

    return dfs(0)


# SOLUTION 2: Dynamic Programming (Bottom-Up)
# ------------------ O(n^2) TC ----------- O(n) SC --------
def canJump_dp(nums):
    n = len(nums)
    dp = [False] * n
    dp[-1] = True  # last index is always reachable

    for i in range(n - 2, -1, -1):
        furthest_jump = min(i + nums[i], n - 1)
        for j in range(i + 1, furthest_jump + 1):
            if dp[j]:
                dp[i] = True
                break
    return dp[0]


# SOLUTION 3: Greedy (Forward Reachable)
# ------------------ O(n) TC ----------- O(1) SC --------
def canJump_greedy(nums):
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:  # stuck
            return False
        farthest = max(farthest, i + jump)
    return True


# SOLUTION 4: Greedy (Backward Goal)
# ------------------ O(n) TC ----------- O(1) SC --------
def canJump_backward(nums):
    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


# ------------------ DRIVER CODE ------------------
if __name__ == "__main__":
    tests = [
        ([2,3,1,1,4], True),
        ([3,2,1,0,4], False),
        ([0], True),
        ([2,0,0], True),
        ([1,2,0,1,0,0], False),
    ]

    for nums, expected in tests:
        print(f"nums = {nums}")
        print("DFS:", canJump_dfs(nums))
        print("DP:", canJump_dp(nums))
        print("Greedy Forward:", canJump_greedy(nums))
        print("Greedy Backward:", canJump_backward(nums))
        print(f"Expected: {expected}\n")
