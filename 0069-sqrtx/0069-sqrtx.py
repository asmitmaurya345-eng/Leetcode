class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x
        l=1
        r=x
        ans=0
        while l<=r:
            m=(l+r)//2
            n=m*m
            if n==x:
                return m
            elif x<n:
                r=m-1
            else:
                l=m+1
                ans=m
        return ans