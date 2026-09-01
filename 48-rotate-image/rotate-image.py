class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n-1):
            for j in range(i+1,m):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        for i in range(n):
            matrix[i]=matrix[i][::-1]
    
        