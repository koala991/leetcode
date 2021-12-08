from typing import List
from itertools import product


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        nrow, ncol = len(grid), len(grid[0])
        visited = [[False] * ncol for _ in range(nrow)]
        visit_stack = [(row, col)] # DFS
        boundary = []
        while len(visit_stack) > 0:
            r, c = visit_stack.pop()
            curr_color, is_boundary = grid[r][c], False
            for next_r, next_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if next_r < 0 or next_r >= nrow:
                    is_boundary = True
                    continue
                if next_c < 0 or next_c >= ncol:
                    is_boundary = True
                    continue
                if visited[next_r][next_c]:
                    continue
                if grid[next_r][next_c] == curr_color and not visited[next_r][next_c]:
                    visit_stack.append((next_r, next_c))
                else:
                    is_boundary = True
            if is_boundary:
                boundary.append((r, c))
            visited[r][c] = True
        while len(boundary) > 0:
            r, c = boundary.pop()
            grid[r][c] = color
        return grid


if __name__ == "__main__":
    grid = [[1,1,1],[1,1,1],[1,1,1]]
    row = 1
    col = 1
    color = 2
    ans = Solution().colorBorder(grid, row, col, color)
    print(ans)
