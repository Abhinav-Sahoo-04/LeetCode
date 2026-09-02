class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for j in range(1,numRows+1):
            res = [1]
            ans = 1
            for i in range(1, j - 1):
                ans = ans * (j - i) // i
                res.append(ans)
            if j!=1:
                res.append(1)
            result.append(res)
        return result