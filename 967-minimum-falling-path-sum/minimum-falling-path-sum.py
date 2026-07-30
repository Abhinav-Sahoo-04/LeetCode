class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def MinimumFallingPath(m,n):
            dp = [-1]*n
            prev=dp[:]
            for i in range(m):
                for j in range(n):
                    if i==0 :
                        dp[j]=matrix[i][j]
                    else:
                        d=matrix[i][j]+prev[j]
                        ld=float("inf")
                        rd=float("inf")
                        if j>0:
                            ld=matrix[i][j]+prev[j-1]
                        if j<n-1:
                            rd=matrix[i][j]+prev[j+1]
                        dp[j]=min(d,ld,rd)
                prev=dp[:]
            return min(dp)
        m=len(matrix)
        n=len(matrix[0])
        return MinimumFallingPath(m,n)


