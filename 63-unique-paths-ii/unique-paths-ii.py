class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        temp=[0]*n
        for i in range(m):
            prev=0
            for j in range(n):
                if i>=0 and j>=0 and obstacleGrid[i][j]==1:
                    temp[j]=0
                elif i==0 and j==0 :
                    temp[j]=1
                else:
                    up=temp[j]
                    left=prev
                    temp[j]=up+left
                prev=temp[j]
        return temp[-1]
