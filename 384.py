"""
1. use random.shuffle
2. switch each possible pairs manually
"""
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.origin = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        temp = self.origin[:]
        # use shuffle method
        random.shuffle(temp)
        # or
        """
        for i in range(len(temp)):
            _i = random.randint(0, i)
            temp[i], temp[_i] = temp[_i], temp[i]
        """
        return temp