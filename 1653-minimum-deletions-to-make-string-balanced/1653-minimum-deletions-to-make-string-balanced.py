class Solution(object):
    def minimumDeletions(self, s):
        dcount=0
        bc=0
        for x in s:
            if x =="b":
                bc+=1
            else:
                dcount=min(dcount+1,bc)
        return dcount