class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def MinimumPathSum(m,n):
            temp=[-1]*n
            best=0
            for i in range(m):
                prev=0
                for j in range(n):
                    if i==0 and j==0:
                        temp[j]=grid[0][0]
                    else:
                        up = float("inf")
                        left = float("inf")
                        if i > 0:
                            up = temp[j] + grid[i][j]
                        if j > 0:
                            left = prev + grid[i][j]
                        temp[j] = min(up,left)
                    prev=temp[j]
            return temp[-1]
        m=len(grid)
        n=len(grid[0])
        return MinimumPathSum(m,n)
        