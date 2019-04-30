# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur_node1 = l1
        cur_node2 = l2
        head_node = ListNode(None)
        cur_node = head_node
        while cur_node1 is not None and cur_node2 is not None:
            if cur_node1.val < cur_node2.val:
                cur_node.next = cur_node1
                cur_node1 = cur_node1.next
            else:
                cur_node.next = cur_node2
                cur_node2 = cur_node2.next
            cur_node = cur_node.next
            cur_node.next = None
        if cur_node1 is not None:
            cur_node.next = cur_node1
        else:
            cur_node.next = cur_node2
        head_node = head_node.next
        return head_node





