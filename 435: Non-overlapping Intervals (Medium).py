# SOLUTION 1
# ------------------ O(nlogn) TC ----------- O(1) SC --------
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])       
        prev_end = float('-inf')
        count = 0
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                count += 1
        return count

# SOLUTION 2
# ------------------ O(nlogn) TC ----------- O(1) SC --------

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1

        return n - count
