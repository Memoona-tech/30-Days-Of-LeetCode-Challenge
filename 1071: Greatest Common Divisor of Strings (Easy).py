# Solution 1

# ----------------------- O(n+m) TC ---------------  O(n + m) SC ------------
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        L = gcd(len(str1),len(str2))
        return str1[:L]
                
{
  The concatenation check takes O(n + m) time (where n = len(str1), m = len(str2)).
  Computing math.gcd(len(str1), len(str2)) is O(log min(n, m)).
  Slicing str1[:L] is O(L) ≤ O(n + m).

SO OVERALL: 
  O(n+m) + O(log min(n,m)) + O(n+m) = O(n+m).
}


        
