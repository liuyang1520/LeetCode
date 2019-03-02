"""
1. Use zip function to pair two process list, got TLE
2. Use dictionary to store child processes, still got TLE
3. Refactor the process of building the processes dictionary with one for loop
"""
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        res = []
        queue = [kill]
        ppzip = zip(pid, ppid)
        while queue:
            temp = queue.pop(0)
            res.append(temp)
            for pair in ppzip:
                if pair[1] == temp:
                    queue.append(pair[0])
        return res


class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        res = []
        queue = [kill]
        ppzip = zip(pid, ppid)
        ppDict = {i: [pair[0] for pair in ppzip if pair[1] == i] for i in ppid}
        while queue:
            temp = queue.pop(0)
            res.append(temp)
            childList = ppDict[temp] if temp in ppDict else []
            queue.extend(childList)
        return res


class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        res = []
        queue = [kill]
        ppzip = zip(pid, ppid)
        ppDict = {}
        for pair in ppzip:
            if pair[1] in ppDict:
                ppDict[pair[1]].append(pair[0])
            else:
                ppDict[pair[1]] = [pair[0]]
        while queue:
            temp = queue.pop(0)
            res.append(temp)
            childList = ppDict[temp] if temp in ppDict else []
            queue.extend(childList)
        return res
