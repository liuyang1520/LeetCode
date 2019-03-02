"""
Note need to output all possible values when there is a tie
"""
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        restDict = {}
        min_index_sum, res = 2000, []
        for i in range(len(list1)):
            restDict[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in restDict:
                if min_index_sum > i + restDict[list2[i]]:
                    min_index_sum = i + restDict[list2[i]]
                    res = [list2[i]]
                elif min_index_sum == i + restDict[list2[i]]:
                    res.append(list2[i])
        return res
