class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def MinimumCoins(coins,amount):
            m=len(coins)
            dp=[0]*(amount+1)
            for i in range(amount+1):
                if i%coins[0]==0:
                    dp[i]=1
            for i in range(1,m):
                for j in range(coins[i],amount+1):
                    notTake=dp[j]
                    take=0
                    if coins[i]<=j:
                        take=dp[j-coins[i]]
                    dp[j]=take+notTake
            return dp[amount]
        
        return MinimumCoins(coins,amount)