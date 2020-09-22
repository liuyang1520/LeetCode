"""
@difficulty: medium
@tags: permutation
@notes: use bitmap as mask for solving the problem
"""
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.bitmap = (1 << len(self.chars)) - 1
        self.cl = combinationLength

    def next(self) -> str:
        while self.bitmap > 0:
            binBitmap = bin(self.bitmap)[2:]
            if binBitmap.count("1") != self.cl:
                self.bitmap -= 1
            else:
                res = []
                binBitmap = "0" * (len(self.chars) - len(binBitmap)) + binBitmap
                for i in range(len(binBitmap)):
                    if binBitmap[i] == "1":
                        res.append(self.chars[i])
                self.bitmap -= 1
                return "".join(res)

    def hasNext(self) -> bool:
        return self.bitmap > (1 << self.cl) - 1
