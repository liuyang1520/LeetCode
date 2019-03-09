class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changes = {5: 0, 10: 0, 20: 0}
        for i in bills:
            if i == 10:
                if changes[5]:
                    changes[5] -= 1
                else:
                    return False
            elif i == 20:
                if changes[10] and changes[5]:
                    changes[5] -= 1
                    changes[10] -= 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False
            changes[i] += 1
        return True
