class Solution(object):
    def climbStairs(self, n):
        if n<3:
            return n
        a=1
        b=2
        for x in range(3,n+1):
            c=a+b
            a=b
            b=c
        return b