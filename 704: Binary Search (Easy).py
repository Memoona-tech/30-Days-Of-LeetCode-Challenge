# Solution
# ------------- O(log n) TC ---------- O(1) SC ----------

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        end = len(nums)-1

        while st <= end:
            mid = (st + end) // 2

            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                end = mid - 1

            else:
                st = mid + 1

        return -1
                
