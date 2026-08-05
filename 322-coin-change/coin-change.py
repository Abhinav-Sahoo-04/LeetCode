class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def MinimumCoins(coins,amount):
            m=len(coins)
            dp=[0]*(amount+1)
            for i in range(amount+1):
                if i%coins[0]==0:
                    dp[i]=i//coins[0]
                else:
                    dp[i]=float("inf")
            for i in range(1,m):
                for j in range(coins[i],amount+1):
                    notTake=dp[j]
                    take=float("inf")
                    if coins[i]<=j:
                        take=1+dp[j-coins[i]]
                    dp[j]=min(take,notTake)
            return  dp[amount] if dp[amount]!=float("inf") else -1
        
        return MinimumCoins(coins,amount)
        