class Solution(object):
    def merge(self, nums1, m, nums2, n):
        n=n+1
        for x in range(-1,-n,-1):
            nums1[x]=nums2[x]
        nums1.sort()