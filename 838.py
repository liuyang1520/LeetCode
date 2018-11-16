"""
Always find the next domino and change values within the range
"""
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = list(dominoes)
        length = len(dominoes)
        cur = 0
        nextD = [length] * length
        last = length
        # stores the index of next L/R for quick reference
        for i in range(length - 1, -1, -1):
            nextD[i] = last
            if dominoes[i] != '.':
                last = i
        # for each pair of LR and assign the values within the range
        while cur < length - 1:
            if dominoes[cur] == '.':
                i = nextD[cur]
                if i == length:
                    break
                elif dominoes[i] == 'L':
                    dominoes[cur:i] = ['L'] * (i - cur)
                    cur = i + 1
                else:
                    cur = i
            elif dominoes[cur] == 'L':
                cur += 1
            else:
                i = nextD[cur]
                if i == length:
                    dominoes[cur:i] = ['R'] * (i - cur)
                    break
                elif dominoes[i] == 'R':
                    dominoes[cur:i] = ['R'] * (i - cur)
                    cur = i
                else:
                    for j in range(cur+1, i):
                        diff = (j - cur) - (i - j)
                        if diff < 0:
                            dominoes[j] = 'R'
                        elif diff > 0:
                            dominoes[j] = 'L'
                    cur = i + 1
        return ''.join(dominoes)
