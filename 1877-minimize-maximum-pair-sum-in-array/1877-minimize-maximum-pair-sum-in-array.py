class Solution(object):
    def minPairSum(self, nums):
        l1=sorted(nums)
        l2=[0]
        n=len(l1)/2
        for x in range(n):
            l2.append((l1.pop(0))+(l1.pop()))
        return max(l2)