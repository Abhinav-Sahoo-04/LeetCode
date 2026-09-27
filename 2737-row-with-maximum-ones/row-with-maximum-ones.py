class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row=[0,0]
        count=0
        for i in range(len(mat)):
            ones=0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    ones+=1
            if ones>count:
                row=[i,ones]
                count=ones
        return row  
        