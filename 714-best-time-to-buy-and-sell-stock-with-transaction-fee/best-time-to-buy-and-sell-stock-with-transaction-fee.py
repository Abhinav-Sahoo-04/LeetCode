class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        i=len(prices)
        dp=[0]*2
        prev=dp[:]
        for a in range(i-1,-1,-1):
            for b in range(2):
                if b==1:
                    dp[b]=max(-prices[a]+prev[0],prev[1])
                else:
                    dp[b]=max(prices[a]-fee+prev[1],prev[0])
            prev=dp[:]
        return dp[1]