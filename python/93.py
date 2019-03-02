# DFS problem.
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValidIP(ip):
            nums = ip.split(".")
            for i in nums:
                if str(int(i)) != i or int(i) > 255:
                    return False
            return True
            
        res = []
        
        def restoreHelper(ip, pos, depth):
            if depth == 3:
                if isValidIP(ip):
                    res.append(ip)
                return
            if len(ip) - pos - 1 <= 3 - depth:
                return
            for i in range(pos + 1, min(len(ip) - 1, pos + 4)):
                restoreHelper(ip[:i+1] + "." + ip[i+1:], i+1, depth + 1)
                
        restoreHelper(s, -1, 0)
        return res