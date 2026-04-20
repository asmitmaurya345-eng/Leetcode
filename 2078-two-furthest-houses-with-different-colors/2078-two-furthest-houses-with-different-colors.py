class Solution(object):
    def maxDistance(self, colors):
        n1=len(colors)
        n2=n1
        i,j=0,0
        maxn=0
        while i<n1 and j<n2:
            if colors[i]!=colors[j]:
                if abs(j-i)>maxn:
                    maxn=j-i
            j+=1
            if j==n2:
                i+=1
                j=0
        return maxn
        