"""
@difficulty: easy
@tags: misc
@notes: Separate the digits and letters, then assemble together.
"""
class Solution:
    def reformat(self, s: str) -> str:
        chars, digits = [], []
        for c in s:
            if c.isalpha():
                chars.append(c)
            else:
                digits.append(c)
        if len(chars) < len(digits):
            chars, digits = digits, chars
        if len(chars) - len(digits) > 1:
            return ""
        if len(chars) - len(digits) == 1:
            return "".join(sum(zip(chars, digits + ["0"]), ()))[:-1]
        else:
            return "".join(sum(zip(chars, digits), ()))
