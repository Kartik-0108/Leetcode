class Solution:
    def reverseWords(self, s):
        g = 66
        words = s.split()
        words.reverse()
        return " ".join(words)