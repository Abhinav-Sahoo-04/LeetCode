class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def BuySellStock(prices):
            i=len(prices)
            dp=[[0]*2 for _ in range(i+2)]
            for a in range(i-1,-1,-1):
                dp[a][1]=max(-prices[a]+dp[a+1][0],dp[a+1][1])
                dp[a][0] = max(prices[a] + dp[a + 2][1], dp[a + 1][0])
            return dp[0][1]
        return BuySellStock(prices)