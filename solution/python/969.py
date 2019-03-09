"""
@difficulty: medium
@tags: misc
@notes: First flip the largest number to the index 0, then flip it to the end. Only need to deal with length-1 list in next round.
"""
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        flips = []
        length = len(A)
        for val in range(length, 0, -1):
            index = A.index(val)
            if index == 0:
                flips.append(val)
                A = A[:val][::-1]
            elif index == val - 1:
                pass
            else:
                flips.append(index + 1)
                flips.append(val)
                A = A[:index+1][::-1] + A[index+1:]
                A = A[:val][::-1]
        return flips
