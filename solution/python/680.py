"""
Methods:
1. recursive
2. string reverse + copy
3. two iterations, left -> right and right -> left, when choose which to delete, try both directions
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(s, direction):
            left, right = 0, len(s) - 1
            canDeleteOne = True
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                elif canDeleteOne:
                    if direction == 'left' and s[left+1] == s[right]:
                        left += 1
                        canDeleteOne = False
                    elif direction == 'right' and s[left] == s[right - 1]:
                        right -= 1
                        canDeleteOne = False
                    else:
                        return False
                else:
                    return False
            return True
        return helper(s, 'left') or helper(s, 'right')
