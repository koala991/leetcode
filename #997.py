from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        status = defaultdict(lambda: [0, 0])
        for _t in trust:
            status[_t[0]][0] = 1
            status[_t[1]][1] += 1
        for i in range(n):
            _trust, _be_trust = status.get(i + 1, [0, 0])
            if _trust == 0 and _be_trust == n - 1:
                return i + 1
        return -1


if __name__ == "__main__":
    n = 2
    trust = [[1,2]]
    ans = Solution().findJudge(n, trust)
    print("Answer:", ans)
