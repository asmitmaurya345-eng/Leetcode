class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x
        elif x==2 or x==3:
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
        else:
            l=2
            r=x//2
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