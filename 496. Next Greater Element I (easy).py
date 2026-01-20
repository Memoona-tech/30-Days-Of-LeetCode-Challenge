# SOLUTION 1
# ------------------ O(n+m) TC ----------- O(m+m) SC --------

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pos = {num: i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = pos[val]
                res[idx] = cur
            if cur in pos:
                stack.append(cur)
        return res
                                    #OR
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}     # value -> next greater value
        stack = []

        for cur in nums2:
            while stack and cur > stack[-1]:
                val = stack.pop()
                next_greater[val] = cur
            stack.append(cur)

        return [next_greater.get(x, -1) for x in nums1]


# SOLUTION 2
# ------------------ O(m*n) TC ----------- O(1) SC --------

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []

        for x in nums1:
            found = False
            for i in range(len(nums2)):
                if nums2[i] == x:
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > x:
                            res.append(nums2[j])
                            found = True
                            break
                    break
            if not found:
                res.append(-1)

        return res
                                      #OR (same)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            x = nums1[i]
            for i in range(len(nums2)):                
                if nums2[i] == x:
                    j = i+1
                    while j < len(nums2):
                        if nums2[j] > x:
                            res.append(nums2[j])
                            break
                        j += 1
                    else:
                        res.append(-1)
        return res

# SOLUTION 3
# ------------------ O(m*n) TC ----------- O(n) SC --------

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        pos = {num: i for i, num in enumerate(nums2)}
        res = [-1] * len(nums1

        for i in range(len(nums2)):
            if nums2[i] not in pos:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = pos[nums2[i]]
                    res[idx] = nums2[j]
                    break
            res.append(ans)

        return res

