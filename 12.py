# Acutually, there are many ways of Roman numeral expressions. We use a dictionary for convenience.
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        dic = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        i = 0
        while num:
            while num >= dic[i][0]:
                num -= dic[i][0]
                roman += dic[i][1]
            i += 1
        return roman