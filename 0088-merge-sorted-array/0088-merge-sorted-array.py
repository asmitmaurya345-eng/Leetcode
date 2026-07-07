class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for x in range(-1,-n-1,-1):
            nums1[x]=nums2[x]
        nums1.sort()