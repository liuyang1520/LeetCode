# Very wierd edge cases:
# [""], ["", ""]
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strDict = {}
        emptyStrNumber = 0
        for i in strs:
            if not i:
                emptyStrNumber += 1
                continue
            sortedStr = "".join(sorted(i))
            if sortedStr not in strDict:
                strDict[sortedStr] = [i]
            else:
                strDict[sortedStr].append(i)
        return [i for i in strDict.values()] + [[""] * emptyStrNumber] if emptyStrNumber > 0 else [i for i in strDict.values()]