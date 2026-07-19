class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        for x in set(nums):
            if nums.count(x)>n/2:
                return x