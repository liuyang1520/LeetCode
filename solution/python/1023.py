"""
@difficulty: medium
@tags: misc
@notes: Use two pointers to compare the query and pattern.
"""
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def isMatch(pattern: str, query: str) -> bool:
            if len(pattern) > len(query):
                return False
            i = j = 0
            while i < len(pattern) and j < len(query):
                print(i, j)
                if pattern[i] == query[j]:
                    i += 1
                    j += 1
                elif query[j].islower():
                    j += 1
                else:
                    return False
            if i < len(pattern):
                return False
            if j < len(query):
                return query[j:].islower()
            return True
        return map(lambda x: isMatch(pattern, x), queries)
