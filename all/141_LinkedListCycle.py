# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        if cur == None or cur.next == None:
            return False
        fastP = cur
        slowP = cur
        while True:
            if fastP.next == None or fastP.next.next == None:
                return False
            fastP = fastP.next.next
            slowP = slowP.next
            if fastP is slowP:
                return True
        return hasCirc

