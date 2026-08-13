class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def WildcardMatching(s1,s2):
            i=len(s1)
            j=len(s2)
            dp=[False]*(j+1)
            dp[0]=True
            for b in range(1,j+1):
                dp[b]=False
            prev=dp[:]
            for a in range(1,i+1):
                flag=True
                for k in range(a):
                    if s1[k]!="*":
                        flag=False
                        break
                dp[0]=flag
                for b in range(1,j+1):
                    if s1[a-1]==s2[b-1] or s1[a-1]=="?":
                        dp[b]=prev[b-1]
                    elif s1[a-1]=="*":
                        dp[b]=dp[b-1] or prev[b]
                    else:
                        dp[b]=False
                prev=dp[:]
            return dp[j]
        return WildcardMatching(p,s)