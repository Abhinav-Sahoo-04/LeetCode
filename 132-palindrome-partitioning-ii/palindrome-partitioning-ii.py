class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            mini=float("inf")
            temp=""
            rev=""
            for k in range(i,n):
                temp+=s[k]
                rev=s[k]+rev
                if temp==rev:
                    cost=1+dp[k+1]
                    mini=min(cost,mini)
            dp[i]=mini
        return dp[0]-1
        