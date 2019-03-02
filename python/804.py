"""
Use set to get count of unique morse codes
"""
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        results = set()
        for word in words:
            morse = "".join([morseCode[ord(i) - 97] for i in word])
            results.add(morse)
        return len(results)
