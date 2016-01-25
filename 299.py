# 1) Find common characters A, 2) Use hashmap to calculate B.
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        length = len(secret)
        A = 0
        B = 0
        s_dict = {}
        g_dict = {}
        for i in range(length):
            if secret[i] == guess[i]:
                A += 1
        for i in secret:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] += 1
        for i in guess:
            if i not in g_dict:
                g_dict[i] = 1
            else:
                g_dict[i] += 1
        for i in range(10):
            i = str(i)
            if i in s_dict and i in g_dict:
                B += min(s_dict[i], g_dict[i])
        B -= A
        return str(A) + "A" + str(B) + "B"