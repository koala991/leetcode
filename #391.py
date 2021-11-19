from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if len(rectangles) <= 1:
            return True
        x, y, a, b = rectangles[0]
        ld = [(x, y), (x, y)]
        rd = [(a, y), (a, y)]
        lu = [(x, b), (x, b)]
        ru = [(a, b), (a, b)]
        aera = (a - x) * (b - y)
        for x, y, a, b in rectangles[1:]:
            if x <= ld[0][0]:
                ld[0] = (x, min(y, ld[0][1]))
            if y <= ld[1][1]:
                ld[1] = (min(x, ld[1][0]), y)
            if a >= rd[0][0]:
                rd[0] = (a, min(y, rd[0][1]))
            if y <= rd[1][1]:
                rd[1] = (max(a, rd[1][0]), y)
            if x <= lu[0][0]:
                lu[0] = (x, max(b, lu[0][1]))
            if b >= lu[1][1]:
                lu[1] = (min(x, lu[1][0]), b)
            if a >= ru[0][0]:
                ru[0] = (a, max(ru[0][1], b))
            if b >= ru[1][1]:
                ru[1] = (max(a, ru[1][0]), b)
            aera += (a - x) * (b - y)
        if not all(map(lambda x: self.is_tuple_equal(*x), [ld, rd, lu, ru])):
            return False
        if ld[0][1] != rd[0][1] or lu[0][1] != ru[0][1] or ld[0][0] != lu[0][0] or rd[0][0] != ru[0][0]:
            return False
        return aera == (ru[0][0] - ld[0][0]) * (ru[0][1] - ld[0][1])

    def is_tuple_equal(self, a, b):
        for i, v_a in enumerate(a):
            if v_a != b[i]:
                return False
        return True

if __name__ == "__main__":
    # rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
    # rectangles = [[0,0,2,2],[1,1,3,3],[2,0,3,1],[0,3,3,4]]
    # rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
    rectangles = [[0,0,2,2],[1,1,3,3],[2,0,3,1],[0,3,3,4]]
    
    ans = Solution().isRectangleCover(rectangles)
    print(ans)
