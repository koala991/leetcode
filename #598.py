from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_i, min_j = m, n
        for i, j in ops:
            min_i = min(i, min_i)
            min_j = min(j, min_j)
        return min_i * min_j


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n
        return min(map(lambda x: x[0], ops)) * min(map(lambda x: x[1], ops))
