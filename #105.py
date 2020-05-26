# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        in_index_root = inorder.index(preorder[0])
        len_l, len_r = in_index_root, len(inorder) - in_index_root - 1 # in_index_root - 0 + 1 - 1, len(inorder) - in_index_root - 1
        root = TreeNode(preorder[0])
        # root.left = self.buildTree(preorder[1: 1 + len_l], inorder[in_index_root - len_l: in_index_root])
        # root.right = self.buildTree(preorder[len(preorder) - len_r: len(preorder)], inorder[in_index_root + 1: in_index_root + len_r + 1])
        if len_l > 0:
            root.left = self.buildTree(preorder[1: 1 + len_l], inorder[:len_l])
        if len_r > 0:
            root.right = self.buildTree(preorder[-len_r:], inorder[-len_r:])
        return root


if __name__ == "__main__":
    preorder = [1,2,3]
    inorder = [3,2,1]
    tree = Solution().buildTree(preorder, inorder)
    print(tree)


