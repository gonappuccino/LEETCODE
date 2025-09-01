class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf] * amount #inf = impossible
        
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c and dp[i-c] != inf:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[amount] if dp[amount] != inf else -1