class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        s1=strs[0]
        a=len(strs)-1
        s2=strs[a]
        x=0
        while x< len(s1) and s1[x]==s2[x]:
            x+=1
        if x>0:
            return s1[:x]
        else:
            return ""