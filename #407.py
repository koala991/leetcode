# 未解答
from typing import List
from itertools import chain


class Matrix(object):
    def __init__(self, matrix):
        super(Matrix, self).__init__()
        self._value = matrix
        self.shape = (len(matrix), len(matrix[0]))

    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            return self._value[index[0]][index[1]]
        else:
            raise TypeError()

    def __setitem__(self, index, value):
        if isinstance(index, tuple) and len(index) == 2:
            self._value[index[0]][index[1]] = value
        else:
            raise TypeError()

    def __repr__(self):
        return self._value.__repr__()

    @staticmethod
    def create(shape, init_value):
        if len(shape) == 2:
            return Matrix([[init_value] * shape[1] for _ in range(shape[0])])
        else:
            raise ValueError()            

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        pool_size = 0
        for floor in range(min(chain(*heightMap)) + 1, max(chain(*heightMap)) + 1):
            pit_map = Matrix([[h < floor for h in l] for l in heightMap])
            pool_size += self.check_pool(pit_map)
        return pool_size

    def check_pool(self, pit_map: Matrix):
        pool_size = 0
        visit_map = Matrix.create(pit_map.shape, False)
        for step in range(pit_map.shape[0] * pit_map.shape[1]):
            i, j = divmod(step, pit_map.shape[1])
            if visit_map[i, j]:
                continue
            if pit_map[i, j]:
                pool_size += self.check_popl_size_DFS((i, j), pit_map, visit_map)
            visit_map[i, j] = True
        return pool_size

    def check_popl_size_DFS(self, position, pit_map: Matrix, visit_map: Matrix):
        leaking, pool_size = False, 0
        visit_queue = [position]
        while len(visit_queue) > 0:
            i, j = visit_queue.pop()
            if visit_map[i, j]:
                continue
            pool_size += 1
            visit_map[i, j] = True
            for i_n, j_n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= i_n < pit_map.shape[0] and 0 <= j_n < pit_map.shape[1]:
                    if pit_map[i_n, j_n]:
                        visit_queue.append((i_n, j_n))
                else:
                    leaking = True
        return 0 if leaking else pool_size