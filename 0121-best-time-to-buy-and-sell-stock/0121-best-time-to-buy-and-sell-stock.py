class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = float('inf')
        max_profit = 0

        for p in prices:
            if p < start:
                start = p
            max_profit = max(max_profit, p - start)
        return max_profit

        