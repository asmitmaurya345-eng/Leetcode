class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for x in nums:
                if target<x:
                    return(nums.index(x))
            else:
                return len(nums)