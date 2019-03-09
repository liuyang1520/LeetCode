"""
DFS search
1. use a string "0101001" to indicate the current state, which numbers are still available
2. prune the cases
3. each action will create a new state, if any substate (new state) is false, then it means the current state can win by performing the action; only if all substates are true, which means no matter what you do, you opponent will win, then we mark current state to false.
"""
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        self.maxInt = maxChoosableInteger
        self.memorize = {}
        return self.canIWinHelper("1"*maxChoosableInteger, desiredTotal)
        
        
    def canIWinHelper(self, state, target):
        subTotal = 0
        for i in range(self.maxInt, 0, -1):
            if state[i-1] == "1":
                if i >= target:
                    self.memorize[state] = True
                    return True
                subTotal += i
        if subTotal < target:
            self.memorize[state] = False
            return False
        for i in range(self.maxInt):
            if state[i] == "1":
                newstate = state[:i] + "0" + state[i+1:]
                if newstate not in self.memorize:
                    self.memorize[newstate] = self.canIWinHelper(newstate, target-i-1)
                if not self.memorize[newstate]:
                    self.memorize[state] = True
                    return True
        self.memorize[state] = False
        return False