"""
Memories + backtrack
1. Translate price into special for convenience, got TLE
2. Refactor with same idea
"""
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def helper(needs, subsum):
            if needs in visited:
                return subsum + visited[needs]
            for s in filteredSpecial:
                newNeeds = tuple(needs[i] - s[i] for i in range(len(needs)))
                if min(newNeeds) < 0:
                    continue
                else:
                    visited[needs] = min(helper(newNeeds, subsum + s[-1]), visited[needs])
            return visited[needs]

        if sum(price) == 0:
            return 0
        from collections import defaultdict
        visited = defaultdict(lambda: float('inf'))
        for i in range(len(price)):
            temp = [0] * (len(price) + 1)
            temp[-1] = price[i]
            temp[i] = 1
            special.append(temp)
        filteredSpecial = []
        for s in special:
            if all(needs[i] >= s[i] for i in range(len(needs))):
                filteredSpecial.append(s)
                visited[tuple(s[:-1])] = min(s[-1], visited[tuple(s[:-1])])
        res = helper(tuple(needs), 0)
        if res == float('inf'):
            return 0
        else:
            return res

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def helper(needs):
            if needs in visited:
                return visited[needs]
            visited[needs] = sum(a * b for a, b in zip(needs, price))
            for s in special:
                newNeeds = tuple(needs[i] - s[i] for i in range(len(needs)))
                if min(newNeeds) < 0:
                    continue
                else:
                    visited[needs] = min(helper(newNeeds) + s[-1], visited[needs])
            return visited[needs]

        if sum(price) == 0:
            return 0
        from collections import defaultdict
        visited = defaultdict(lambda: float('inf'))
        res = helper(tuple(needs))
        if res == float('inf'):
            return 0
        else:
            return res
