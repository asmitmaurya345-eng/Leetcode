import fractions
class Solution(object):
    def findGCD(self, nums):
        n1=max(nums)
        n2=min(nums)
        #return fractions.gcd(n1,n2)
        while n2!=0:
            n1,n2=n2,n1%n2
        return n1