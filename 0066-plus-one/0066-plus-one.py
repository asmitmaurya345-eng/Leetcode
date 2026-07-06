class Solution(object):
    def plusOne(self, digits):
        n=0
        newnum=[]
        for x in digits:
            n=n*10+x
        n=n+1
        while n!=0:
            newnum.insert(0,n%10)
            n=n//10
        return newnum