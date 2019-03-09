"""
Solution 1, TLE, sort then iterate by picking the heaviest and just-work weight to the boat, O(n^2)
Solution 2, greedy, sort then pick the heaviest and lightest to the boat, O(nlogn)
"""
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        visited = set()
        people.sort(reverse=True)
        for i in range(len(people)):
            addToBoat = False
            if i in visited:
                continue
            for j in range(i+1, len(people)):
                if j not in visited and people[i] + people[j] <= limit:
                    boats += 1
                    addToBoat = True
                    visited.update({i, j})
                    break
            if not addToBoat:
                boats += 1
                visited.update({i})
        return boats

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        people.sort(reverse=True)
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
            boats += 1
        return boats
