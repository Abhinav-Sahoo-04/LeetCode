class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        i=len(word1)
        j=len(word2)
        dp=[0]*(j+1)
        for a in range(1,i+1):
            prev=0
            for b in range(1,j+1):
                temp=dp[b]
                if word1[a-1]==word2[b-1]:
                    dp[b]=prev+1
                else:
                    dp[b]=max(dp[b],dp[b-1])
                prev=temp
        return i+j-(2*dp[j])