# SOLUTION 1
# ------------------ O(n) TC ----------- O(n+m) -> n==m so SC = O(n) SC --------

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for ch, word in zip(pattern, words):
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False
            char_to_word[ch] = word
            word_to_char[word] = ch

        return True
