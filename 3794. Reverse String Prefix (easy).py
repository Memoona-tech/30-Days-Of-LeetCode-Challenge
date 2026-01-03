# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def reverseStringPrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]

# SOLUTION 2
# ------------------ O(n) TC ----------- O()n SC --------

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        ss = list(s)
        l, r = 0, k-1
        while l <= r and r < len(s):
            ss[l], ss[r] = ss[r], ss[l]
            l += 1
            r -= 1
        return "".join(ss)

# SOLUTION 3 (C++)
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution {
public:
    string reversePrefix(string s, int k) {
        reverse(s.begin(),s.begin()+k);
        return s;
    }
};
