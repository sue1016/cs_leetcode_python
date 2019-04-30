# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        cur_node = head
        next_node = cur_node.next
        while next_node is not None:
            if cur_node.val == next_node.val:
                cur_node.next = next_node.next
                next_node = cur_node.next
            else:
                cur_node = next_node
                next_node = cur_node.next
        return head
