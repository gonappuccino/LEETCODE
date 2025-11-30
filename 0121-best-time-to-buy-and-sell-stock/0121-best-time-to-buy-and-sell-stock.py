class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = float('inf')
        max_profit = 0

        for price in prices:
            if price < left:
                left = price
            max_profit = max(max_profit, price - left)
        return max_profit