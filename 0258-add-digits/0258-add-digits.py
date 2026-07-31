class Solution(object):
    def addDigits(self, num):
        a=0
        if num > 9:
            while num:
                a+=num%10
                num //= 10
            num = a
            a=0
        if num > 9:
            while num:
                a+=num%10
                num //= 10
            num = a
            a=0
        if num > 9:
            while num:
                a+=num%10
                num //= 10
            num = a
            a=0
        return num