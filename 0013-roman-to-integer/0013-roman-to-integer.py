class Solution(object):
    def romanToInt(self, s):
        n=0
        a=len(s)
        for x in range (a):
            if s[x]=="I":
                if s[x:x+2]=='IV':
                    n+=-1
                elif s[x:x+2]=='IX':
                    n+=-1
                else:
                    n+=1
            elif s[x]=="V":
                n+=5
            elif s[x]=="X":
                if s[x:x+2]=='XL':
                    n+=-10
                elif s[x:x+2]=='XC':
                    n+=-10
                else:
                    n+=10
            elif s[x]=="L":
                n+=50
            elif s[x]=="C":
                if s[x:x+2]=='CD':
                    n+=-100
                elif s[x:x+2]=='CM':
                    n+=-100
                else:
                    n+=100
            elif s[x]=="D":
                n+=500
            elif s[x]=="M":
                n+=1000
            elif s[x]==" ":
                break
        return n