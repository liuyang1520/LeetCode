"""
@difficulty: easy
@tags: misc
@notes: use two pointers to locate the previous start point and current end point.
"""
class OrderedStream:
    def __init__(self, n: int):
        self.array = [None] * (n + 1)
        self.n = n
        self.prev = 1
        self.cur = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.array[id] = value
        hasValue = False
        while self.cur <= self.n and self.array[self.cur]:
            self.cur += 1
            hasValue = True
        if hasValue:
            temp = self.prev
            self.prev = self.cur
            return self.array[temp: self.cur]
        return []
