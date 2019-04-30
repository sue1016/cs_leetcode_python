# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            maxW = 1
            layer = []
            root_pair = root,0
            layer.append(root_pair)
            while layer:
                layer_size = len(layer)
                for counter in range(layer_size):
                    cur_pair = layer.pop(0)
                    cur_node = cur_pair[0]
                    cur_index = cur_pair[1]
                    left = cur_node.left
                    right = cur_node.right
                    if left:
                        layer.append((left,2*cur_index))
                    if right:
                        layer.append((right,2*cur_index+1))
                left_hand_index = 0
                right_hand_index = 0
                if layer:
                    left_hand_index = layer[0][1]
                    right_hand_index = layer[-1][1]
                thisW = right_hand_index - left_hand_index + 1
                if thisW > maxW:
                    maxW = thisW
            return maxW


