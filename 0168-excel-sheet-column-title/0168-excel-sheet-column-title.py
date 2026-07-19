class Solution(object):
    def convertToTitle(self, columnNumber):
        a=[]
        while columnNumber>0:
            columnNumber-=1
            char=columnNumber%26
            a.append(chr(char+65))
            columnNumber//=26
        return "".join(a[::-1])