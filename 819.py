"""
Need to change unicode string to normal string, otherwise translate won't work
"""
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.encode('ascii','ignore')
        pureWords = paragraph.translate(None, "!?',;.")
        counter = {}
        for word in pureWords.split(" "):
            lower = word.lower()
            if lower not in banned:
                if lower not in counter:
                    counter[lower] = 1
                else:
                    counter[lower] += 1
        return max(counter, key= counter.get)
