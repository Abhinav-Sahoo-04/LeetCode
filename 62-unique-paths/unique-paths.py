class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        temp=[0]*n
        for i in range(m):
            prev=0
            for j in range(n):
                if i==0 and j==0:
                    temp[j]=1
                else:
                    up=temp[j]
                    left=prev
                    temp[j]=up+left
                prev=temp[j]
        return temp[-1]
        