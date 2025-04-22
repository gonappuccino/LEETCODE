class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # 가장 싸게 살 수 있는 날 업데이트
            else:
                max_profit = max(max_profit, price - min_price)  # 현재 가격으로 팔았을 때 이익 계산

        return max_profit

            