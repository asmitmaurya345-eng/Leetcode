class Solution(object):
    def removeElement(self, nums, val):
        k=0
        a=len(nums)
        for i in range(a):
            if nums[i] != val:
                nums[k] = nums[i]  # Move it to the front
                k += 1
        return k