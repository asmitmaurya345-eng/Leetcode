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
                clh=h[l]
                l+=1
                while l<r and h[l]<=clh:
                    l+=1
            else:
                crh=h[r]
                r-=1
                while l<r and h[r]<=crh:
                    r-=1
        return maxw