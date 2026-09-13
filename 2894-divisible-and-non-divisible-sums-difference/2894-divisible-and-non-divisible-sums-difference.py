class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n1=0
        n2=0
        for x in range(n+1):
            n1+=x
        for y in range(m,n+1,m):
            n2+=y
        return n1-(2*n2)