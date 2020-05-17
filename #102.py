# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue, output = [], []
        queue.append(root)
        queue.append(None)   
        while len(queue) > 0:
            this_level = []
            while True:
                curr = queue.pop(0)

                if curr is None: break
                # if len(queue) == 0 or curr is None: break

                this_level.append(curr.val)

                if curr.left is not None: queue.append(curr.left)
                if curr.right is not None: queue.append(curr.right)

            output.append(this_level)
            if len(queue) > 0: queue.append(None) 

        return output
        