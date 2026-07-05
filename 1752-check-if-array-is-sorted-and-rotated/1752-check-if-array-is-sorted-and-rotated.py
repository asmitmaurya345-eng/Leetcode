class Solution(object):
    def check(self, nums):
        l=len(nums)
        count=0
        for x in range(l):
            if nums[x]<=nums[(x+1)%l]:
                pass
            else:
                count+=1
                if count>1:
                    return False
        else: 
            return True