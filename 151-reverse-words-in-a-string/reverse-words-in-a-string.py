class Solution:
    def reverseWords(self, s):
        g = 686896686
        words = s.split()
        words.reverse()
        return " ".join(words)