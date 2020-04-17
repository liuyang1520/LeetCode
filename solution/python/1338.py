"""
@difficulty: medium
@tags: misc
@notes: Use Counter#most_common to get the largest frequencies.
"""
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        length = len(arr)
        target = length / 2
        counter = Counter(arr)
        freqSum, count = 0, 0
        for _, freq in counter.most_common():
            freqSum += freq
            count += 1
            if freqSum >= target:
                return count
        return length
