"""
Using stack: [function_id, current_time, wasted_time]
Initially, each wasted_time is 0, whenever a nested function ends, the wasted_time changes by plusing the time used to run that function
"""
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        for log in logs:
            f_id, f_status, f_time = log.split(":")
            f_id = int(f_id)
            current_time = int(f_time) if f_status == 'start' else int(f_time) + 1
            if f_status == 'start':
                stack.append([f_id, current_time, 0])
            else:
                last = stack.pop()
                res[last[0]] += current_time - last[1] - last[2]
                if stack:
                    peek = stack[-1]
                    peek[2] += current_time - last[1]
        return res
