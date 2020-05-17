# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isBSTBetween(root, INT_MIN, INT_MAX)

    def isBSTBetween(self, root, a_min, a_max):
        is_valid_root = a_min < root.val < a_max
        is_valid_l, is_valid_r = True, True
        if root.left is not None:
            is_valid_l = self.isBSTBetween(root.left, a_min, root.val) 
        if root.right is not None:
            is_valid_r = self.isBSTBetween(root.right, root.val, a_max)
        return is_valid_root and is_valid_l and is_valid_r 
            
