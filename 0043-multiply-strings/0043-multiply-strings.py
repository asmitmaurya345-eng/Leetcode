class Solution(object):
    def multiply(self, num1, num2):
        n1=0
        n2=0
        number=[48,49,50,51,52,53,54,55,56,57]
        for x in num1:
            n1=n1*10+ord(x)-48
        for x in num2:
            n2=n2*10+ord(x)-48
        return str(n1*n2)