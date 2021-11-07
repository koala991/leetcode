from collections import defaultdict
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        for candy in candyType:
            counter[candy] += 1
            if len(counter) >= len(candyType) / 2:
                break
        return len(counter)
