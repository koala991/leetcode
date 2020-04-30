class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profile = 0
        min_price = prices[0]
        for price in prices:
            if price - min_price > max_profile:
                max_profile = price - min_price
            if price < min_price:
                min_price = price
        return max_profile