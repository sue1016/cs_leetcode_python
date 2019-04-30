# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLen(self,head):
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count = count + 1
        return count

    def forwardToSame(self,headA, headB):
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)
        if lenA > lenB:
            cur = headA
            for i in range(abs(lenA-lenB)):
                cur = cur.next
            return cur,headB
        else:
            cur = headB
            for i in range(abs(lenA-lenB)):
                cur = cur.next
            return headA,cur


    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        curA,curB = self.forwardToSame(headA,headB)
        while curA is not None and curA is not curB:
            curA = curA.next
            curB = curB.next
        if curA is None:
            return None
        else:
            return curA



