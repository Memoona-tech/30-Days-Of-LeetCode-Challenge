# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]
        max_avg = curr_sum/k

        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            avg = curr_sum / k
            max_avg = max(max_avg, avg)
        
        return max_avg


# SOLUTION 2
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[:k])

        # Start the loop from the kth element 
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]
            
            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k
