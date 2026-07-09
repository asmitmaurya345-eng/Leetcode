class Solution(object):
    def reverse(self, x):
        a=-1 if x<0 else 1
        ri=a*int(str(abs(x))[::-1])
        if ri<-2**31 or ri>2**31-1:
            return 0
        return ri