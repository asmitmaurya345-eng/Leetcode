# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head=ListNode(0)
        a=head
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            sum_=v1+v2+carry
            a.next=ListNode(sum_%10)
            a=a.next
            carry=sum_//10
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return head.next