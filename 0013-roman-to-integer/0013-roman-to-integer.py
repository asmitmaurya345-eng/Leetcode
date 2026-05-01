class Solution(object):
    def romanToInt(self, s):
        s=s+" "*10000
        n=0
        a=len(s)
        for x in range (a):
            if s[x]=="I":
                if s[x:x+2]=='IV':
                    n+=4
                    s=s[:x+1]+s[x+2:]
                elif s[x:x+2]=='IX':
                    n+=9
                    s=s[:x+1]+s[x+2:]
                else:
                    n+=1
            elif s[x]=="V":
                n+=5
            elif s[x]=="X":
                if s[x:x+2]=='XL':
                    n+=40
                    s=s[:x+1]+s[x+2:]
                elif s[x:x+2]=='XC':
                    n+=90
                    s=s[:x+1]+s[x+2:]
                else:
                    n+=10
            elif s[x]=="L":
                n+=50
            elif s[x]=="C":
                if s[x:x+2]=='CD':
                    n+=400
                    s=s[:x+1]+s[x+2:]
                elif s[x:x+2]=='CM':
                    n+=900
                    s=s[:x+1]+s[x+2:]
                else:
                    n+=100
            elif s[x]=="D":
                n+=500
            elif s[x]=="M":
                n+=1000
            elif s[x]==" ":
                break
        return n