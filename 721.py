"""
Set and merge. Also can be solved more efficiently with disjoint-set data structure
"""
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        stats = defaultdict(list)
        for row in accounts:
            name, emails = row[0], set(row[1:])
            isNew, prev = True, 0
            for i in range(len(stats[name])-1, -1, -1):
                if emails & stats[name][i]:
                    if isNew:
                        stats[name][i] |= emails
                        prev = i
                    else:
                        stats[name][prev] |= stats[name][i]
                        del stats[name][i]
                        prev -= 1
                        stats[name]
                    isNew = False
            if isNew:
                stats[name].append(emails)
        res = []
        for name in stats:
            for emails in stats[name]:
                res.append([name] + sorted(emails))
        return res
