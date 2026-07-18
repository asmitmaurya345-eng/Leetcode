import fractions
class Solution(object):
    def findGCD(self, nums):
        n1=min(nums)
        n2=max(nums)
        return fractions.gcd(n1,n2)
        