"""
@difficulty: easy
@tags: misc
@notes: Or using #replace method.
"""
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return "[.]".join(address.split("."))
