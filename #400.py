class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n
        i, cum_nums = 1, self.countNums(1)
        while cum_nums < n:
            i += 1
            cum_nums += self.countNums(i)
        cum_nums -= self.countNums(i)
        a, b = divmod(n - cum_nums - 1, i)
        return int(str(10 ** (i - 1) + a)[int(b)])

    def countNums(self, i):
        return i * 9 * 10 ** (i - 1) if i >= 1 else 0
