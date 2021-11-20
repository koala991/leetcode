"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        max_depth = 0
        search_stack = [(root, 1)]
        while len(search_stack) > 0:
            node, depth = search_stack.pop()
            if node.children:
                search_stack += list(map(lambda x: (x, depth + 1), node.children))
            else:
                max_depth = max(depth, max_depth)
        return max_depth