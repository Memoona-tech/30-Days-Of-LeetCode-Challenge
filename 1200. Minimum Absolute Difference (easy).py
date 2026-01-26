# SOLUTION 1
# ------------------ O(nlogn) TC ----------- O(1) SC --------

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_dif = float('inf')

        for i in range(1, len(arr)):
            min_dif = min(min_dif, abs(arr[i]-arr[i-1]))

        for i in range(1, len(arr)):
            if (arr[i]-arr[i-1]) == min_dif:
                res.append([arr[i-1],arr[i]])

        return res  

# SOLUTION 2
# ------------------ O(nlogn) TC ----------- O(1) SC --------
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_dif = float('inf')

        for i in range(1, len(arr)):
            dif = abs(arr[i]-arr[i-1])

            if dif < min_dif:
                min_dif = dif
                res = [[arr[i-1],arr[i]]]

            elif (arr[i]-arr[i-1]) == min_dif:
                res.append([arr[i-1],arr[i]])

        return res  

# SOLUTION 3
# ------------------ O(n^2) TC ----------- O(1) SC --------

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        min_dif = float('inf')
        res = []

        for i in range(n):
            for j in range(i+1, n):
                diff = abs(arr[i] - arr[j])
                if diff < min_dif:
                    min_dif = diff
                    res = [[min(arr[i], arr[j]), max(arr[i], arr[j])]]
                elif diff == min_dif:
                    res.append([min(arr[i], arr[j]), max(arr[i], arr[j])])

        return sorted(res)
