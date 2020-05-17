# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
暴力DFS 时间复杂度 O(|s|*|t|)
另外两种 O(|s| + |t|)的解法
1. 数补空值序列化+KMP算法比较字符串
2. 树HASH
"""
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        output = False
        if self.isSame(s, t):
            output = True
        elif s.left is not None and self.isSubtree(s.left, t):
            output = True
        elif s.right is not None and self.isSubtree(s.right, t):
            output = True
        return output

    def isSame(self, a, b):
        if a is None and b is None:
            return True
        elif a is None or b is None:
            return False
        else:
            return a.val == b.val and self.isSame(a.left, b.left) and self.isSame(a.right, b.right)