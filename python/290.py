# Use a dictionary to map the pattern with str, remember to check the duplications of values in the end.
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split(" ")
        if len(pattern) != len(strs):
            return False
        dict = {}
        for i in range(len(pattern)):
            if pattern[i] not in dict:
                dict[pattern[i]] = strs[i]
            else:
                if dict[pattern[i]] != strs[i]:
                    return False
        if len(set(dict.values())) != len(dict.values()):
            return False
        return True