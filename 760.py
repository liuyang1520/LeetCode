"""
Put value/position pairs in hash table for better performance
"""
class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = []
        position = {}
        for i in range(len(B)):
            position[B[i]] = i
        return [position[i] for i in A]
