class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digitLogs = [log for log in logs if log[-1].isdigit()]
        letterLogs = [log for log in logs if not log[-1].isdigit()]
        letterLogs.sort(key=lambda x: x.split()[1:] + x.split()[0:1])
        return letterLogs + digitLogs
