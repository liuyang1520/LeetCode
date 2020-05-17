"""
@difficulty: medium
@tags: misc
@notes: Brute-force + memorization
"""
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memorize = {1: 1}
        def getPower(num):
            init = num
            if num == 1:
                return 1
            count = 0
            while num != 1:
                if num in memorize:
                    memorize[init] = count + memorize[num]
                    return count + memorize[num]
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
                count += 1
            return count
        powers = []
        for i in range(lo, hi + 1):
            powers.append([i, getPower(i)])
        powers.sort(key=lambda x: x[1])
        return powers[k-1][0]
