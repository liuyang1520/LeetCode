# A hard problem when dealing with various cases.
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        try:
            str = str.strip()
            for i in str:
                if not (i == "+" or i == "-" or (ord("0") <= ord(i) <= ord("9"))):
                    str = str[: str.index(i)]
                    break
            res = int(str)
            if res > 2147483647:
                return 2147483647
            elif res < -2147483648:
                return -2147483648
            else:
                return res
        except:
            return 0