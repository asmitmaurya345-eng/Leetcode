class Solution(object):
    def checkString(self, s):
        b=0
        for x in s:
            if x=="b":
                b+=1
            elif b!=0:
                return False
        else:
            return True
