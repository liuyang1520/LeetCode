"""
Iterate the string and store unmatched indexes
"""
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        from collections import Counter
        diffIndex = []
        if len(A) != len(B) or len(A) < 2: return False
        for i in range(len(A)):
            if A[i] != B[i]:
                diffIndex.append(i)
        if not diffIndex:
            return True if Counter(A).most_common(1)[0][1] >= 2 else False
        elif len(diffIndex) == 2:
            x, y = diffIndex[0], diffIndex[1]
            return True if A[:x] + A[y] + A[x+1:y] + A[x] + A[y+1:] == B else False
        else:
            return False
