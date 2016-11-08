"""
while:
    find min height with people[i][1] is 0
    append to answer
    update other people
end

Tricky solution:
https://discuss.leetcode.com/topic/60394/easy-concept-with-python-c-java-solution
"""
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in people:
            i.append(i[1])
        count, res = 0, []
        while people:
            # find min height with 0 people in front
            minElement = [float("inf"), 0, 0]
            for i in people:
                if i[0] < minElement[0] and i[2] == 0:
                    minElement = i
            res.append([minElement[0], minElement[1]])
            people.remove(minElement)
            # update other people
            for i in people:
                if i[0] <= minElement[0]:
                    i[2] -= 1
        return res