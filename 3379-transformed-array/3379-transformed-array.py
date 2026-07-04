class Solution(object):
    def constructTransformedArray(self, nums):
        result=[]
        n=len(nums)
        for i in range(n):
            result.append(nums[(i+nums[i])%n])
        return result