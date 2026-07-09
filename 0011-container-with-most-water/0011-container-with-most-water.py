class Solution(object):
    def maxArea(self, h):
        l=0
        r=len(h)-1
        maxw=0
        while l<r:
            w=r-l
            hight=min(h[l],h[r])
            area=w*hight
            maxw=max(maxw,area)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return maxw