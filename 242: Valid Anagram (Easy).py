# Solution 1  ......
# --------------------------- O(n) TC ------------- O(n) SC ------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts1 = Counter(s)    # O(n) time, O(n) space
        counts2 = Counter(t)    # O(n) time, O(n) space
        if counts1 == counts2:
            return True
        return False

# { class Solution:
#   def isAnagram(self, s: str, t: str) -> bool:  
#       return Counter(s) == Counter(t) }              ................... same as above

# Solution 2
#-------------------------- O(n) TC ---------------- O(1) SC -----------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0]*26

        for char_s, char_t in zip(s,t):
            freq[ord(char_s) - ord('a')] += 1
            freq[ord(char_t) - ord('a')] -= 1
        return all(count == 0 for count in freq)



# EXPLAINATION BY CHATGPT
{
  Think of your `freq` list as 26 boxes labeled 0 through 25:

```
 index:  0  1  2  …  25
 letter: a  b  c  …   z
```

You need a way to turn any lowercase letter (`'a'` through `'z'`) into the corresponding box number:

1. **`ord(ch)`** gives you the Unicode code point (an integer) of the character `ch`.

   * For example, `ord('a')` is 97, `ord('b')` is 98, …, `ord('z')` is 122.

2. **Subtracting `ord('a')`** shifts that range down to start at 0:

   * `ord('a') - ord('a') = 97 - 97 = 0`
   * `ord('b') - ord('a') = 98 - 97 = 1`
   * …
   * `ord('z') - ord('a') = 122 - 97 = 25`

So:

```python
index = ord(ch) - ord('a')
```

gives you exactly the spot in your `freq` list that corresponds to the letter `ch`.

* If `ch == 'a'`, `index == 0`.
* If `ch == 'm'`, `index == 12`.
* If `ch == 'z'`, `index == 25`.

That way you can do `freq[index] += 1` (or `-= 1`) for any letter, without writing a giant `if/elif` chain for each character.

}



