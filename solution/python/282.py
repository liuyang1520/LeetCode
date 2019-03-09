# DFS problem, treating multiply as the highest priority.
# http://bookshadow.com/weblog/2015/09/16/leetcode-expression-add-operators/
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def checkValid(nums):
            if nums.startswith("00"):
                return False
            elif nums.startswith("0") and int(nums):
                return False
            return True
        
        def addOperatorsHelper(num, target, mulExpression, mulRightValue):
            res = []
            if checkValid(num):
                if int(num) * mulRightValue == target:
                    res += [num + mulExpression]
            for i in range(1, len(num)):
                left, right = num[:i], num[i:]
                if not checkValid(right):
                    continue
                rightExpression = right + mulExpression
                rightValue = int(right) * mulRightValue
                for j in addOperatorsHelper(left, target - rightValue, "", 1):
                    res += [j + "+" + rightExpression]
                for j in addOperatorsHelper(left, target + rightValue, "", 1):
                    res += [j + "-" + rightExpression]
                for j in addOperatorsHelper(left, target, "*" + rightExpression, rightValue):
                    res += [j]
            return res
        if not num:
            return []
        return addOperatorsHelper(num, target, "", 1)