class Solution(object):
    def longestCommonPrefix(self, strs):
        s1=min(strs)
        s2=max(strs)
        x=0
        while x< len(s1) and s1[x]==s2[x]:
            x+=1
        if x>0:
            return s1[:x]
        else:
            return ""