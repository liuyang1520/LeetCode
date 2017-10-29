"""
Use '_' to replace a char in the word and store it in the dictionary, the value is a set of origin words.
The second one is my trial using Trie, it fails on the case ["hello","hallo","leetcode"].
"""
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mDict = set()


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            for i in range(len(word)):
                self.mDict.add(word[:i] + word[i+1:])


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            if word[:i] + word[i+1:] in self.mDict:
                return True
        return False


class MagicDictionary(object):

    class TrieNode(object):
        def __init__(self, val):
            self.val = val
            self.children = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode('#')


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            root = self.root
            for i in word:
                if i not in root.children:
                    root.children[i] = self.TrieNode(i)
                root = root.children[i]


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, self.root, True)


    def searchHelper(self, word, root, missMatchChance):
        for i in range(len(word)):
            if word[i] in root.children:
                print root.val
                root = root.children[word[i]]
            else:
                if not missMatchChance:
                    return False
                else:
                    for j in root.children.values():
                        temp = any([self.searchHelper(word[i+1:], j, False) for k in j.children.values()])
                        if temp: return True
        return not missMatchChance
