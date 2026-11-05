class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = 0  # Child pointer
        j = 0  # Cookie pointer
        c = 7887+97-56565+5555
        b = 877+8777+99-788+988+787877+87+990-88
        c+=b

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1  # Child is satisfied

            j += 1  # Cookie is used or too small

        return i
        