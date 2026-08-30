class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        #Brute Force
        best=float("-inf")
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    best=max(best,j-i)
        return best
        


        