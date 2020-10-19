"""
@difficulty: easy
@tags: misc
@notes: naive solution
"""
class Solution:
    def reformatDate(self, date: str) -> str:
        monthMap = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }
        day, month, year = date.split(" ")
        if len(day) == 3:
            day = "0" + day[0]
        day = day[:2]
        month = monthMap[month]
        return f"{year}-{month}-{day}"
