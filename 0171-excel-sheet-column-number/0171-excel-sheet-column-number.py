class Solution(object):
    def titleToNumber(self, columnTitle):
        a = 0
        for x in columnTitle:
            n = ord(x) - 64
            a = a * 26 + n
        return a