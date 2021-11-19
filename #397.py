minimum = {1: 0, 2: 1}

class Solution:
    def integerReplacement(self, n: int) -> int:
        if n in minimum:
            return minimum.get(n)
        if n & 1:
            ans = 1 + min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))
        else:
            ans = 1 + self.integerReplacement(n >> 1)
        minimum[n] = ans
        return ans