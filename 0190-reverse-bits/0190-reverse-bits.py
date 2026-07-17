class Solution(object):
    def reverseBits(self, n):
        a=bin(n)[2:].zfill(32)
        return int(a[::-1],2)