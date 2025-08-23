# SOLUTION 2 RUNS KINDA FAST IN PRACTICE BUT BOTH ARE SAME TC & SC
# SOLUTION 1
# ------------------ O(n+m) TC ----------- O(1) SC --------

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineLet = Counter(magazine)
        for i in ransomNote:
            if magazineLet[i] <= 0:
                return False           
            magazineLet[i] -= 1
        return True

# SOLUTION 1
# ------------------ O(n+m) TC ----------- O(1) SC --------

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0]*26

        for i in magazine:
            count[ord(i)-97] += 1
        for i in ransomNote:
            count[ord(i)-97] -= 1
            if count[ord(i)-97] < 0:
                return False
        return True

        
