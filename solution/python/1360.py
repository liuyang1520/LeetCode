"""
@difficulty: easy
@tags: misc
@notes: Use datetime lib for convenience, or calculate the leap year/month myself.
"""
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import datetime
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2 - d1).days)
