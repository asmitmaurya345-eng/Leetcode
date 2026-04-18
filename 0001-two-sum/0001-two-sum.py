import copy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        d=0
        nums1= copy.deepcopy(nums)
        for x in nums:
            n=1
            d+=1
            if n==1:
                nums1.pop(0)
            for y in nums1:
                if x+y==target:
                    return [nums.index(x),nums1.index(y)+d]
            n=0