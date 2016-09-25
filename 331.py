"""
Cut the leaves iteratively, 4 # # -> #
9,3,4,#,#,1,#,#,2,#,6,#,#
9,3,4,#,#
9,3,#
9,3,#,1,#,#
9,3,#,#
9,#
9,#,2,#,6,#,#
9,#,2,#,#
9,#,#
#
Valid string should return # finally
"""
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        stack = []
        pos = 0
        while pos < len(nodes):
            stack.append(nodes[pos])
            while len(stack) >= 3 and stack[-2:] == ["#", "#"] and stack[-3] != "#":
                stack = stack[:-3] + ["#"]
            pos += 1
        if stack == ["#"]:
            return True
        return False


"""
https://discuss.leetcode.com/topic/35976/7-lines-easy-java-solution
Init degree = 1, any "#" uses 1 out-degree thus degree--, any node brings 2 out-degree and uses 1 thus degree++.
If degree < 0 or (degree == 0 and not at the end), no node can be added to the tree, error.
In the end, degree should be 0.
"""
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        availableDegree = 1
        for i in range(len(nodes)):
            if nodes[i] != "#":
                availableDegree += 1
            else:
                availableDegree -= 1
            if availableDegree < 0 or (availableDegree == 0 and i < len(nodes) - 1):
                return False
        if availableDegree != 0:
            return False
        return True


