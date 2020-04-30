
class Solution:
    # def totalNQueens(self, n: int) -> int:
    def totalNQueens(self, n):
        self.nq = n
        self.put = []
        return self.putQueen(0)

    def checkDiag(self, row):
        output = True
        col = len(self.put)
        for _c, _r in enumerate(self.put):
            if abs(row - _r) == abs(col - _c):
                output = False
                break
        return output

    def putQueen(self, k):
        """
        return: nums of correct situation with self.put while calling
        """
        output = 0
        if k >= self.nq:
            output += 1
        else:
            for i in filter(lambda x: x not in self.put, range(self.nq)) :
                if self.checkDiag(i):
                    self.put.append(i)
                    output += self.putQueen(k + 1)
                    self.put.remove(i)
        return output

if __name__ == "__main__":
    solver = Solution()
    n = 4
    print(solver.totalNQueens(n))
