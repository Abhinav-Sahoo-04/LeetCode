class Solution:
    def minInsertions(self, s: str) -> int:
        s1=s
        s2=s[::-1]
        i=len(s1)
        j=len(s2)
        dp=[0]*(j+1)
        for a in range(1,i+1):
            prev=0
            for b in range(1,j+1):
                temp=dp[b]
                if s1[a-1]==s2[b-1]:
                    dp[b]=prev+1
                else:
                    dp[b]=max(dp[b],dp[b-1])
                prev=temp
        return i - dp[j]
        