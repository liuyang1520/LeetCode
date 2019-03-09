"""
O(n) time + O(n) space at least
char[:] can replace whole list in place easily
"""
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result = ""
        i = 0
        while i < len(chars):
            last = chars[i]
            result += last
            j = i
            while j+1 < len(chars) and chars[j+1] == last:
                j += 1
            count = j - i + 1
            if count > 1:
                result += str(count)
            i = j + 1
        chars[:] = list(result)
        return len(result)
