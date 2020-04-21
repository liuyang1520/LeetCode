"""
@difficulty: medium
@tags: Trie
@notes: Trie + DFS
"""
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        import collections
        # define Trie
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        for f in folder:
            dirs = f.split("/")[1:]
            temp, prev = trie, None
            for d in dirs:
                prev = temp
                if temp[d] is not None:
                    temp = temp[d]
                else:
                    break
            # truncate trie to the current longest
            prev[d] = None
        res = []
        # dfs to gather all folders
        def dfs(trie, paths):
            if trie is None:
                return res.append("/" + "/".join(paths))
            for i in trie:
                dfs(trie[i], paths + [i])
        dfs(trie, [])
        return res
