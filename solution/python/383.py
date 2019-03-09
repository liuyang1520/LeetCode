"""
hashset or dictionary or Counter
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        ran = Counter(ransomNote)
        mag = Counter(magazine)
        for i in ran:
            if i not in mag or mag[i] < ran[i]:
                return False
        return True