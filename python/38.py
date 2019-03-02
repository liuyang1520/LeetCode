# Naive solution, iteratively generating the sequences.
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = "1"
        while n > 1:
            seq = self.seqGene(seq)
            n -= 1
        return seq
        
        
    def seqGene(self, num):
        if len(num) <= 1:
            return "1" + num
        count = 1
        seq = num[0]
        for i in range(1, len(num)):
            if num[i] == num[i - 1]:
                count += 1
            else:
                seq = seq[:-1] + str(count) + seq[-1] + num[i]
                count = 1
            if i == len(num) - 1:
                seq = seq[:-1] + str(count) + seq[-1]
        return seq