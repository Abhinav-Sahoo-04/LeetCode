class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts=[0]+sorted(cuts)+[n]
        m=len(cuts)
        dp=[[0]*m for _ in range(m)]
        for i in range(m-2,0,-1):
            for j in range(i,m-1):
                mini=float("inf")
                for k in range(i,j+1):
                    cost=(cuts[j+1]-cuts[i-1])+dp[i][k-1]+dp[k+1][j]
                    mini=min(mini,cost)
                dp[i][j]=mini
        return dp[1][m-2]