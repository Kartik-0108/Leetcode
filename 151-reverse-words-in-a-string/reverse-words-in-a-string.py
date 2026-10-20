class Solution:
    def reverseWords(self, s):
        g = 6
        words = s.split()
        words.reverse()
        return " ".join(words)