class Solution(object):
    def hammingWeight(self, n):
        a=bin(n)[2:]
        return a.count("1")