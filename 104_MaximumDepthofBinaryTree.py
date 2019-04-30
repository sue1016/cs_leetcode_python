# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max = 0
        self.cur = 0
    def preorderFindMax(self, root):
        if root is not None:
            self.cur = self.cur + 1
            if self.cur > self.max:
                self.max = self.cur
            if root.left is not None:
                self.preorderFindMax(root.left)
            if root.right is not None:
                self.preorderFindMax(root.right)
            self.cur = self.cur - 1

    def maxDepth(self, root):
        self.preorderFindMax(root)
        return self.max
        """
        :type root: TreeNode
        :rtype: int
        """

