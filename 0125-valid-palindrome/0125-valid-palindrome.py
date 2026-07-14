class Solution(object):
    def isPalindrome(self, a):
        s=""
        for x in a:
            if x.isalnum():
                s=s+x.lower()
        return True if s==s[::-1] else False
