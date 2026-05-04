class Solution(object):
    def isValid(self, s):
        a=["(","{","["]
        b=[0]
        for x in s:
            if x in a:
                b.append(x)
            elif x == ")" and b and b[-1] == "(":
                b.pop()
            elif x == "}" and b and b[-1] == "{":
                b.pop()
            elif x == "]" and b and b[-1] == "[":
                b.pop()
            else :
                return False
        if b==[0]:
            return True
        else:
            return False