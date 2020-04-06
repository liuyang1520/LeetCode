"""
@difficulty: medium
@tags: misc
@notes: Since we only need to the total count,
so we just calculate the combination counts for each elements when it is in the mid.
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        res = 0
        for j in range(1, len(rating) - 1):
            incSub1 = incSub2 = 0
            decSub1 = decSub2 = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    incSub1 += 1
                elif rating[i] > rating[j]:
                    decSub1 += 1
            for k in range(j + 1, len(rating)):
                if rating[j] < rating[k]:
                    incSub2 += 1
                elif rating[j] > rating[k]:
                    decSub2 += 1
            res += incSub1 * incSub2 + decSub1 * decSub2
        return res
