class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def BuySellStock(prices):
            i=len(prices)
            dp=[[0]*(2+1) for _ in range(2)]
            for b in range(2):
                dp[b][0]=0
            for a in range(2):
                for b in range(3):
                    dp[a][b]=0
            prev=[row[:] for row in dp]
            for a in range(i-1,-1,-1):
                for b in range(2):
                    for c in range(1,3):
                        if b==1:
                            profit=max(-prices[a]+prev[0][c],prev[1][c])
                        else:
                            profit = max(prices[a]+prev[1][c-1], prev[0][c])
                        dp[b][c]=profit
                prev = [row[:] for row in dp]
            return dp[1][2]

        return BuySellStock(prices)
        