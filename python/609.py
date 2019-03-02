"""
Straitforword answer, split string and combine into filepath/name, use hash to find duplicates
"""
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        fileDict = {}
        for record in paths:
            info = record.split(' ')
            for i in info[1:]:
                filename = info[0] + '/' + i.split('(')[0]
                filecontent = i.split('(')[1][:-1]
                if filecontent not in fileDict:
                    fileDict[filecontent] = [filename]
                else:
                    fileDict[filecontent].append(filename)
        res = []
        for i in fileDict:
            if len(fileDict[i]) > 1:
                res.append(fileDict[i])
        return res
