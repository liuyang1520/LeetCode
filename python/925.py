"""
Two pointers
"""
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        nameLen, typedLen = len(name), len(typed)
        if nameLen > typedLen or name[0] != typed[0]:
            return False
        iName = iTyped = 0
        while iName < nameLen and iTyped < typedLen:
            if name[iName] == typed[iTyped]:
                iName += 1
                iTyped += 1
            elif typed[iTyped] == typed[iTyped - 1]:
                iTyped += 1
            else:
                return False
        if iName == nameLen and (iTyped == typedLen or all(i==name[-1] for i in typed[iTyped:])):
            return True
        return False
