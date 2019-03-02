"""
1. recursive solution, got MLE.
2. use while loop instead.
"""
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return True
        if len(data) >= 1 and data[0] < 128:
            return self.validUtf8(data[1:])
        elif len(data) >= 2 and 192 <= data[0] < 224 and 128 <= data[1] < 192:
            return self.validUtf8(data[2:])
        elif len(data) >= 3 and 224 <= data[0] < 240 and 128 <= data[1] < 192 and 128 <= data[2] < 192:
            return self.validUtf8(data[3:])
        elif len(data) >= 4 and 240 <= data[0] < 248 and 128 <= data[1] < 192 and 128 <= data[2] < 192 and 128 <= data[3] < 192:
            return self.validUtf8(data[4:])
        else:
            return False


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        while data:
            if len(data) >= 1 and data[0] < 128:
                data = data[1:]
            elif len(data) >= 2 and 192 <= data[0] < 224 and 128 <= data[1] < 192:
                data = data[2:]
            elif len(data) >= 3 and 224 <= data[0] < 240 and 128 <= data[1] < 192 and 128 <= data[2] < 192:
                data = data[3:]
            elif len(data) >= 4 and 240 <= data[0] < 248 and 128 <= data[1] < 192 and 128 <= data[2] < 192 and 128 <= data[3] < 192:
                data = data[4:]
            else:
                return False
        return True