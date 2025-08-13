# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        string = ""
        for i in digits:
            string += str(i)
        res = int(string)+1
        return [int(c) for c in str(res)]
