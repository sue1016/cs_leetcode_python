# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.isSym = True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        self.preRecur(root.left,root.right)
        return self.isSym



    def preRecur(self,tree1,tree2):
        if tree1.val != tree2.val:
            self.isSym = False
            return
        else:

            if tree1.left != None and tree2.right != None:
                self.preRecur(tree1.left,tree2.right)
            elif tree1.left == None and tree2.right == None:
                pass
            else:
                self.isSym = False
                return

            if tree1.right != None and tree2.left != None:
                self.preRecur(tree1.right,tree2.left)
            elif tree1.right == None and tree2.left == None:
                pass
            else:
                self.isSym = False
                return


