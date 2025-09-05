# SOLUTION 1
# ------------------ O(n+m) TC ----------- O(n+m) SC --------

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        def merge(l1, l2):           
            i = j = 0
            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    merged.append(l1[i])
                    i += 1
                else:
                    merged.append(l2[j])
                    j += 1

            if i < len(l1):
                merged.extend(l1[i:])
            if j < len(l2):
                merged.extend(l2[j:])
        
        merge(nums1, nums2)
        n = len(merged)
        mid = n//2
        if n%2 == 1:
            return merged[mid]
        else:
            return ( merged[mid-1] + merged[mid] ) / 2
            
