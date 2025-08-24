class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for price in prices:
            if price < buy:
                buy = price
            maxProfit = max(maxProfit, price - buy)
        return maxProfit