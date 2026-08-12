class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def EditDistance(s1,s2):
            i=len(s1)
            j=len(s2)
            dp=[0]*(j+1)
            for b in range(j+1):
                dp[b]=b
            for a in range(1,i+1):
                prev=dp[0]
                dp[0]=a
                for b in range(1,j+1):
                    temp=dp[b]
                    if s1[a-1]==s2[b-1]:
                        dp[b]=prev
                    else:
                        dp[b]=1+min(dp[b],prev,dp[b-1])
                    prev=temp
            return dp[j]
        return EditDistance(word1,word2)