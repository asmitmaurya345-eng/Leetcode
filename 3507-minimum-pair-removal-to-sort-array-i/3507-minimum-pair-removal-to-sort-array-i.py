class Solution(object):
    def minimumPairRemoval(self, nums):
        turns=0
        n=len(nums)
        for x in range(n):
            if nums==sorted(nums):
                return turns
            else:
                sums=[a + b for a, b in zip(nums, nums[1:])]
                min_=min(sums)
                min_index=sums.index(min_)
                nums.pop(min_index)
                nums.pop(min_index)
                nums.insert(min_index,min_)
                turns+=1