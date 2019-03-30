"""
@difficulty: easy
@tags: permutation
@notes: Brute-force, generate all permutations and compare one by one.
"""
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        def permutation(array):
            res = []
            if not array: return [[]]
            for i in range(len(array)):
                for t in permutation(array[:i] + array[i+1:]):
                    res.append(array[i:i+1] + t)
            return res

        res = permutation(A)
        largest = ""
        for per in res:
            per = map(str, per)
            hour, minute = "".join(per[:2]), "".join(per[2:])
            if int(hour) >= 24 or int(minute) >= 59:
                continue
            time = hour + ":" + minute
            if time >= largest:
                largest = time
        return largest
