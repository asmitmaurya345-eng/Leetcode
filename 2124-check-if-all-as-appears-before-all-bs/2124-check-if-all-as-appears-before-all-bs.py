class Solution(object):
    def checkString(self, s):
        s1=sorted(s)
        if list(s)==s1:
            return True
        else:
            return False