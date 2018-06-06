"""
Use a stack to store and new door numbers
"""
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        total = len(rooms)
        visited = set([0])
        stack = [0]
        while stack:
            room = stack.pop()
            for i in rooms[room]:
                if i not in visited:
                    visited.add(i)
                    stack.append(i)
            if len(visited) == total: return True
        return False
