# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left, right):
        if left is None or right is None:
            return left is None and right is None
        
        return not (left.val != right.val
                    or (not self._isSymmetric(left.left, right.right))
                    or (not self._isSymmetric(left.right, right.left))
                   )

if __name__ == "__main__":
    left = TreeNode(10)
    left.right = TreeNode(3)
    right = TreeNode(10)
    right.right = TreeNode(3) 
    solution = Solution()
    print(solution._isSymmetric(left, right))