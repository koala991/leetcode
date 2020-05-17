# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path, path_p, path_q = [], [], []
        curr, ntimes = (root, 0)
        while len(path) > 0 or curr is not None:
            if curr is None or ntimes > 1:
                curr, ntimes = path.pop(-1)
                continue

            if curr.val == p.val:
                path_p = [node for node, _ in path] + [curr]
            elif curr.val == q.val:
                path_q = [node for node, _ in path] + [curr]

            if ntimes == 0:
                path.append((curr, ntimes + 1))
                curr, ntimes = curr.left, 0
            elif ntimes == 1:
                path.append((curr, ntimes + 1))
                curr, ntimes = curr.right, 0

            if len(path_p) > 0 and len(path_q) > 0: break
        
        output = None
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i].val == path_q[i].val: output = path_q[i]

        return output
        


