class Solution(object):
    def isHappy(self, n):
        c = set()
        while n != 1 and n not in c:
            c.add(n)
            a = 0
            b = n
            while b > 0:
                a += (b % 10) ** 2
                b //= 10
            n = a
        return n == 1