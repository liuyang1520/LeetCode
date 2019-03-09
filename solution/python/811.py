"""
Split to split space and dot
"""
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        stats = {}
        for temp in cpdomains:
            count, domains = temp.split(' ')
            count = int(count)
            domains = domains.split('.')
            for i in range(len(domains)):
                domain = ".".join(domains[-i-1:])
                if domain not in stats:
                    stats[domain] = count
                else:
                    stats[domain] += count
        return [str(stats[key]) + " " + key for key in stats]
