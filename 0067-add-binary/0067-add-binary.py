class Solution(object):
    def addBinary(self, a, b):
        aa=int(a,2)
        bb=int(b,2)
        return(bin(aa+bb)[2:])