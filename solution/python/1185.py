"""
@difficulty: easy
@tags: misc, math
@notes: Use datetime library to cheat.
"""
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime
        return datetime.datetime(year, month, day).strftime("%A")
