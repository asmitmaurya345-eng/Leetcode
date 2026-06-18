class Solution(object):
    def multiply(self, num1, num2):
        n1=0
        n2=0
        number=[48,49,50,51,52,53,54,55,56,57]
        for x in num1:
            n=number.index(ord(x))
            n1=n1*10+n
        for x in num2:
            n=number.index(ord(x))
            n2=n2*10+n
        return str(n1*n2)