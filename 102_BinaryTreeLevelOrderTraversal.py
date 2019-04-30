# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stacks = []
        queue = [root]
        while queue:
            stack = []
            queue_size = len(queue)
            for index in range(queue_size):
                cur_node = queue.pop(0)
                stack.append(cur_node.val)
                left = cur_node.left
                right = cur_node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            stacks.append(stack)
        return stacks



