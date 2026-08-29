class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            dp[i][0]=matrix[i][0]
        for j in range(len(matrix[0])):
            dp[0][j]=matrix[0][j]
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==1 and i-1 >=0 and j-1>=0:
                    is_square=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])
                    matrix[i][j]=is_square+1
        count=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count+=matrix[i][j]
        return count