"""
Brute force + Counter
"""
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        
        def getDistance(p1, p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
            
        res = 0
        distances = [0] * len(points)
        for i in range(len(points)):
            for j in range(len(points)):
                distances[j] = getDistance(points[i], points[j])
            counter = Counter(distances)
            for d in counter:
                if counter[d] > 1:
                    res += counter[d] * (counter[d] - 1)
        return res