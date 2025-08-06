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
