class Solution(object):
    def minPairSum(self, nums):
        l1=sorted(nums)
        l2=[0]
        n=len(l1)/2
        for x in range(n):
            l2.append(l1[x]+l1[-1-x])
        return max(l2)