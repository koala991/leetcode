from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        blind = 0
        for i, t in enumerate(timeSeries):
            if i > 0  and t - timeSeries[i - 1] <= duration:
                blind += t - timeSeries[i - 1]
            else:
                blind += duration
        return blind
