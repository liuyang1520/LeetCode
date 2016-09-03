"""
1) find node with no incoming edges, delete it;
2) if cannot find, then the graph has cycle, return [];
3) repeat 1, 2 until all nodes are deleted.
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        linkDict = {}
        for i in range(numCourses):
            linkDict[i] = [set(), set()]
        for t, s in prerequisites:
            linkDict[t][0].add(s)
            linkDict[s][1].add(t)
        
        res = []
    	hasCycle = False
    	deleted = set()
    	while len(deleted) < numCourses and not hasCycle:
    		hasCycle = True
    		for i in linkDict:
    			if i not in deleted and len(linkDict[i][0]) == 0:
    				hasCycle = False
    				res.append(i)
    				deleted.add(i)
    				for j in linkDict[i][1]:
    					linkDict[j][0].discard(i)
    	return [] if hasCycle else res