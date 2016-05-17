# Iterate the first two possible numbers and construct the whole string, compare to the given one.
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i, j in itertools.combinations(range(len(num) - 1), 2):
            a = num[: i+1]
            b = num[i+1: j+1]
            if str(int(a)) != a or str(int(b)) != b:
                continue
            pos = j + 1
            while pos < len(num):
                temp = int(a) + int(b)
                if str(temp) != num[pos: pos + len(str(temp))]:
                    break
                a = b
                b = temp
                pos += len(str(temp))
            if pos == len(num):
                return True
        return False
