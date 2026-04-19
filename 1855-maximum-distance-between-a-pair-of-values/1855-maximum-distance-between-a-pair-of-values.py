class Solution(object):
    def maxDistance(self, nums1, nums2):
        n1=len(nums1)
        n2=len(nums2)
        i,j=0,0
        maxn=0
        while i<n1 and j<n2:
            if nums1[i]<=nums2[j]:
                if j-i>maxn:
                    maxn=j-i
                j+=1
            else:
                i+=1
            if i>j:
                j=i
        return maxn
        