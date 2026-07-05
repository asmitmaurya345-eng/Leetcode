class Solution(object):
    def removeDuplicates(self, nums):
        n=[]
        n1=[]
        for x in nums:
            if x in n:
                n1.append("_")
            else:
                n.append(x)
        nums[:]=n+n1
        return len(n)