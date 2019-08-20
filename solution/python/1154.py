"""
@difficulty: easy
@tags: misc
@notes: Use datetime library to parse and minus.
"""
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = map(int, date.split("-"))
        from datetime import date
        return (date(year, month, day) - date(year, 1, 1)).days + 1
