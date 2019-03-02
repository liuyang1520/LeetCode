# Resursive solution.
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >= 1000000000:
            return self.numberToWords(num / 1000000000) + " Billion" if num % 1000000000 == 0 else self.numberToWords(num / 1000000000) + " Billion " + self.numberToWords(num % 1000000000)
        if num >= 1000000:
            return self.numberToWords(num / 1000000) + " Million" if num % 1000000 == 0 else self.numberToWords(num / 1000000) + " Million " + self.numberToWords(num % 1000000)
        if num >= 1000:
            return self.numberToWords(num / 1000) + " Thousand" if num % 1000 == 0 else self.numberToWords(num / 1000) + " Thousand " + self.numberToWords(num % 1000)
        if num >= 100:
            return self.numberToWords(num / 100) + " Hundred" if num % 100 == 0 else self.numberToWords(num / 100) + " Hundred " + self.numberToWords(num % 100)
        if num >= 90:
            return "Ninety" if num % 90 == 0 else "Ninety " + self.numberToWords(num % 90)
        if num >= 80:
            return "Eighty" if num % 80 == 0 else "Eighty " + self.numberToWords(num % 80)
        if num >= 70:
            return "Seventy" if num % 70 == 0 else "Seventy " + self.numberToWords(num % 70)
        if num >= 60:
            return "Sixty" if num % 60 == 0 else "Sixty " + self.numberToWords(num % 60)
        if num >= 50:
            return "Fifty" if num % 50 == 0 else "Fifty " + self.numberToWords(num % 50)
        if num >= 40:
            return "Forty" if num % 40 == 0 else "Forty " + self.numberToWords(num % 40)
        if num >= 30:
            return "Thirty" if num % 30 == 0 else "Thirty " + self.numberToWords(num % 30)
        if num >= 20:
            return "Twenty" if num % 20 == 0 else "Twenty " + self.numberToWords(num % 20)
        numToWordsDic = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        return numToWordsDic[num]