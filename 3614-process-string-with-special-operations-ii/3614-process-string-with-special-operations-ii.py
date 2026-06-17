class Solution(object):
    def processStr(self,s,k):
        lengths=[]
        curr_len=0
        for char in s:
            if char.islower():
                curr_len+=1
            elif char=='*':
                curr_len=max(0, curr_len - 1)
            elif char=='#':
                curr_len*=2
            elif char=='%':
                pass
            lengths.append(curr_len)
        if not lengths or k >= lengths[-1]:
            return "."
        for i in range(len(s)-1,-1,-1):
            char=s[i]
            L=lengths[i]
            if char.islower():
                if k==L-1:
                    return char
            elif char=='%':
                k=L-1-k
            elif char=='#':
                prev_L=L//2
                if prev_L>0:
                    k%=prev_L
            elif char=='*':
                pass
        return "."