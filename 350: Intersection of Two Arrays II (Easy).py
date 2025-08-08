# SOLUTION 1
# ------------------ O(n₁ + n₂) TC -----------  O(n₁ + n₂) / O(n₁ + min(n₁, n₂)) SC --------

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        cnt = Counter(nums1)    
        for x in nums2:                
            if cnt[x] > 0:             
                ans.append(x)         
                cnt[x] -= 1           
        return ans

{
Time Complexity:

Building cnt = Counter(nums1) takes O(n₁), where n₁ = len(nums1).

The for x in nums2: loop runs n₂ = len(nums2) iterations, each doing O(1) work (counter lookup, append, decrement).
——— Total: O(n₁ + n₂).

Space Complexity:

The Counter(nums1) uses O(n₁) space in the worst case (one entry per distinct element in nums1).

The output list ans can grow to size up to min(n₁, n₂) if every element intersects.
——— Extra space (aside from the inputs): O(n₁ + min(n₁, n₂)), which is O(n₁ + n₂) in the worst case, but often summarized as O(n₁).

}


# SOLUTION 2
# ------------------ O()O(n1 log n1 + n2 log n2) (≈ O(n log n) when sizes are comparable) TC ----------- O() SC --------
{ TC & SC EXPLANATION: https://chatgpt.com/s/t_6895da56e6b0819189192add878fa338 }
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        l1 = len(nums1)
        l2 = len(nums2)
        i = 0
        j = 0
        res = []
        nums1.sort()
        nums2.sort()

        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
