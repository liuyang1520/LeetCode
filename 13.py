# Add "I" at the end for convenience. But do not add the last number.
# If the next number is larger, should minus current number; else add current number.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        s = s + "I"
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total


# Alternative solution.
# If previsou number is smaller than current number, add current numbeer and minus twice of previous.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i-1]]:
                total += roman[s[i]] - 2 * roman[s[i-1]]
            else:
                total += roman[s[i]]
        return total