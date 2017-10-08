"""
Use a stack instead of the recursive solution.
id = index + 1
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        stack = [id]
        total = 0
        while stack:
            currentEmployee = employees[stack.pop() - 1]
            total += currentEmployee.importance
            stack += currentEmployee.subordinates
        return total
