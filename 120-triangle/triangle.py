class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def Triangle(row):
            temp=[0]*row
            for i in range(row):
                temp[i]=triangle[row-1][i]
            for i in range(row-2,-1,-1):
                for j in range(i+1):
                    down=triangle[i][j]+temp[j]
                    dig=triangle[i][j]+temp[j+1]
                    temp[j]=min(down,dig)
            return temp[0]
        row=len(triangle)
        return Triangle(row)

    
        