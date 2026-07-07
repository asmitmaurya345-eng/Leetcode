class Solution(object):
    def sumAndMultiply(self,n):
        if n<1:
            return 0
        x=0
        sum=0
        n1=list(str(n))
        for i in n1:
            a=int(i)
            if a!=0:
                sum+=a
                x=x*10+a
        return x*sum