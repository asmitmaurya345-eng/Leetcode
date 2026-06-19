class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        l2=[0]
        n=len(nums)/2
        for x in range(n):
            l2.append(nums[x]+nums[-1-x])
        return max(l2)