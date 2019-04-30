# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.isSame = True
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        self.preRecur(p,q)
        return self.isSame


    def preRecur(self,tree1,tree2):
        if tree1.val != tree2.val:
            self.isSame = False
            return
        else:

            if tree1.left != None and tree2.left != None:
                self.preRecur(tree1.left,tree2.left)
            elif tree1.left == None and tree2.left == None:
                pass
            else:
                self.isSame = False
                return

            if tree1.right != None and tree2.right != None:
                self.preRecur(tree1.right,tree2.right)
            elif tree1.right == None and tree2.right == None:
                pass
            else:
                self.isSame = False
                return

