class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def ShortestCommonSupersequence(s1,s2):
            i=len(s1)
            j=len(s2)
            dp=[[0]*(j+1) for _ in range(i+1)]
            for a in range(1,i+1):
                for b in range(1,j+1):
                    if s1[a-1]==s2[b-1]:
                        dp[a][b]=dp[a-1][b-1]+1
                    else:
                        dp[a][b]=max(dp[a-1][b],dp[a][b-1])
            res=[]
            while i>0 and j>0:
                if s1[i-1]==s2[j-1]:
                    res.append(s1[i-1])
                    i-=1
                    j-=1
                else:
                    if dp[i-1][j]>dp[i][j-1]:
                        res.append(s1[i-1])
                        i-=1
                    else:
                        res.append(s2[j-1])
                        j-=1
            while i>0:
                res.append(s1[i-1])
                i-=1
            while j>0:
                res.append(s2[j-1])
                j-=1
            return "".join(res[::-1])
            
        return  ShortestCommonSupersequence(str1,str2)