class Solution(object):
    def groupAnagrams(self, strs):
        a={}
        for x in strs:
            b="".join(sorted(x))
            if b in a:
                a[b]+=[x]
            else:
                a[b]=[x]
        return a.values()