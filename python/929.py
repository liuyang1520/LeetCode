"""
String process + set
"""
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for email in emails:
            local, host = email.split("@")
            local = local.replace(".", "")
            firstPlusSignIndex = local.find("+")
            if firstPlusSignIndex > 0:
                local = local[:firstPlusSignIndex]
            unique.add(local + "@" + host)
        return len(unique)
