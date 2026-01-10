# SOLUTION 1
# ------------------ O(n) TC ----------- O(k) SC --------

class Solution:
    def subarraysDivByK(self, nums, k):
        prefix_sum = 0
        count = 0
        
        # remainder frequency map
        freq = {0: 1}   # prefix_sum % k == 0 initially
        
        for num in nums:
            prefix_sum += num
            rem = prefix_sum % k
            
            # handle negative remainder
            if rem < 0:
                rem += k
            
            # if this remainder appeared before,
            # those many subarrays end here
            count += freq.get(rem, 0)
            
            # update frequency
            freq[rem] = freq.get(rem, 0) + 1
        
        return count
