"""
@difficulty: medium
@tags: misc
@notes: Use a dictionary to store the index: count pair for each element from groupSizes, then divide it into chunks of list.
"""
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupDict = {}
        for i, v in enumerate(groupSizes):
            if v not in groupDict:
                groupDict[v] = [i]
            else:
                groupDict[v].append(i)
        res = []
        for k, v in groupDict.items():
            for i in range(int(len(v) / k)):
                res.append(v[i*k: (i+1)*k])
        return res
