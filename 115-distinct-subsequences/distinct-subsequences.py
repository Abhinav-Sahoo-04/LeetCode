class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def DistinctSubsequance(s1,s2):
            i=len(s1)
            j=len(s2)
            dp=[0]*(j+1)
            dp[0]=1
            for a in range(1,i+1):
                for b in range(j,0,-1):
                    if s1[a-1]==s2[b-1]:
                        dp[b]=dp[b-1]+dp[b]
                    else:
                        dp[b]=dp[b]

            return dp[j]
        return DistinctSubsequance(s,t)