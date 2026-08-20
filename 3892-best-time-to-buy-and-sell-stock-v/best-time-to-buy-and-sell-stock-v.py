class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        i=len(prices)
        dp=[[0]*(k+1) for _ in range(3)]
        for b in range(3):
            dp[b][0]=0
        for a in range(3):
            for b in range(k+1):
                if a==0:
                    dp[0][b]=0
                else:
                    dp[a][b]=float("-inf")
        prev=[row[:] for row in dp]
        for a in range(i-1,-1,-1):
            for c in range(1,k+1):
                dp[0][c]=max(-prices[a]+prev[1][c],prev[0][c],prices[a]+prev[2][c])
                dp[1][c]=max(prev[1][c],prices[a]+prev[0][c-1])
                dp[2][c]=max(prev[2][c],-prices[a]+prev[0][c-1])
                    
            prev=[row[:] for row in dp]
        return dp[0][k]

            