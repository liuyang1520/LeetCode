# Two dictionary stores total word frequency and current frequency during travesal; stop when temp value is larger than total value.
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        freq = {i: words.count(i) for i in set(words)}
        length = len(words[0])
        lengthTotal = len(words[0]) * len(words)
        for i in range(len(s) - lengthTotal + 1):
            temp = {}
            j = i
            while j < i + lengthTotal:
                word = s[j: j+length]
                if word in freq:
                    if word not in temp:
                        temp[word] = 1
                    else:
                        temp[word] += 1
                    if temp[word] > freq[word]:
                        break
                else:
                    break
                j = j + length
            if j == i + lengthTotal:
                res.append(i)
        return res
