class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def CherryPickup(m,n):
            dp=[[-1]*n for _ in range(n)]
            prev=[row[:] for row in dp]
            for i in range(m-1,-1,-1):
                for j in range(n):
                    for k in range(n):
                        if i==m-1:
                            if j==k:
                                dp[j][k]=grid[i][j]
                            else:
                                dp[j][k]=grid[i][j]+grid[i][k]
                        else:
                            maxi=float("-inf")
                            for a in (-1,0,1):
                                for b in (-1,0,1):
                                    if j == k:
                                        val = grid[i][j]
                                    else:
                                        val = grid[i][j] + grid[i][k]
                                    if 0 <= j+a < n and 0 <= k+b < n:
                                        val+=prev[j+a][k+b]
                                    else:
                                        val=float("-inf")
                                    maxi=max(val,maxi)
                            dp[j][k]=maxi
                prev = [row[:] for row in dp]
            return dp[0][n-1]
        m=len(grid)
        n=len(grid[0])
        return CherryPickup(m,n)