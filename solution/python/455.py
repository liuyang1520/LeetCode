class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i, j = 0, 0
        g.sort()
        s.sort()
        count = 0
        
        # two points
        """
        while i < len(g) and j < len(s):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j == len(s):
                break
            if s[j] >= g[i]:
                count += 1
                j += 1
            i += 1
        return count
        """
        
        # a concise version
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
        return count