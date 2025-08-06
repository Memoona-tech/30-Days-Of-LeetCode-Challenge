# Solution 1
# -------------- O(n) TC ------- O(1) SC --------
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1  
        while j >= 0:
            if i >= 0 and nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1


# SOLLUTION 2
# --------------- O((m+n) log(m+n)) TC ------------- O(1) SC
def merge(nums1, m, nums2, n):
    # 1. Copy nums2 values into the back of nums1
    nums1[m:] = nums2[:n]
    # 2. Sort the whole array
    nums1.sort()

# SOLUTION 3
# ------------- O(m+n) TC --------- O() SC

def merge(nums1, m, nums2, n):
    merged = []
    i = j = 0

    # 1. Build merged list
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i]); i += 1
        else:
            merged.append(nums2[j]); j += 1

    # 2. Append leftovers
    merged.extend(nums1[i:m])
    merged.extend(nums2[j:n])

    # 3. Copy back into nums1
    nums1[:] = merged

# SOLUTION 4
# ------------------- O() TC ----------- O() SC

# Insertion via bisect (educational, not recommended)
import bisect
def merge(nums1, m, nums2, n):
    # pretend the trailing zeros aren't there
    nums1[:] = nums1[:m]
    for x in nums2:
        bisect.insort(nums1, x)
    # if you need exactly length m+n:
    # nums1[:] = nums1[:m+n]





