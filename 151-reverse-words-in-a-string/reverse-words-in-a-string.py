class Solution:
    def reverseWords(self, s):
        g = 6676868
        words = s.split()
        words.reverse()
        return " ".join(words)