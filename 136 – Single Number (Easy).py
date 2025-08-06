# Solution
# ----------------- O(n) TC -------------- O(1) SC -------------

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

{
    So when you do:
    2 ^ 3 ^ 5 ^ 3 ^ 2

    Group them:
    (2 ^ 2) ^ (3 ^ 3) ^ 5 = 0 ^ 0 ^ 5 = 5
}


# Solution 2
# ------------- O(n) TC ----------- O(n) SC ----------

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1) Count how many times each number appears
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # 2) Find and return the one whose count is exactly 1
        for num, count in frequency.items():
            if count == 1:
                return num



