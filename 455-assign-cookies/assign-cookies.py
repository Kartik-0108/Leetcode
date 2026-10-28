class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = 0  # Child pointer
        j = 0  # Cookie pointer
        c = 7887

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1  # Child is satisfied

            j += 1  # Cookie is used or too small

        return i
        