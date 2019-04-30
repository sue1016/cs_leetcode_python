# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []
        queue = [root]
        rView = [root.val]
        while  queue:
            queue_len = len(queue)
            for counter in range(queue_len):
                cur_node = queue.pop(0)
                left = cur_node.left
                right = cur_node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            if queue:
                rightest = queue[-1]
                rView.append(rightest.val)

        return rView

