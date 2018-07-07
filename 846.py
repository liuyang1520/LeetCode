"""
Sort numbers and always pick up the first W elements. Need to delete used elements in case there are duplicates.
"""
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        length = len(hand)
        if length % W != 0: return False
        hand.sort()
        stack = []
        i = 0
        count = 0
        while i < len(hand):
            if (not stack) or (len(stack) < W and stack[-1] == hand[i] - 1):
                stack.append(hand[i])
                hand.pop(i)
                i -= 1
            i += 1
            if len(stack) == W:
                stack = []
                count += 1
                i = 0
        if count == length / W:
            return True
        return False
