class Solution(object):
    def removeDuplicates(self, nums):
        a=0
        n=len(nums)
        for x in range(n):
            if nums[a]!=nums[x]:
                a+=1
                nums[a]=nums[x]
        return a+1