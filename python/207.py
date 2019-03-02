# Same as Course Schedule 2
class Solution(object):
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		linkDict = {}
		for i in range(numCourses):
			linkDict[i] = [set(), set()]
		for t, s in prerequisites:
			linkDict[t][0].add(s)
			linkDict[s][1].add(t)
		
		hasCycle = False
		deleted = set()
		while len(deleted) < numCourses and not hasCycle:
			hasCycle = True
			for i in linkDict:
				if i not in deleted and len(linkDict[i][0]) == 0:
					hasCycle = False
					deleted.add(i)
					for j in linkDict[i][1]:
						linkDict[j][0].discard(i)
		return not hasCycle