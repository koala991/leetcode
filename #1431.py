class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # n_max = max(candies)
        n_max = 0
        for _n in candies:
            n_max = max(n_max, _n)

        output = [True if _n + extraCandies >= n_max else False for _n in candies]
        return output
        