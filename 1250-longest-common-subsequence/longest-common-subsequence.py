class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def LongestCommonSubsequence(s1,s2):
            i=len(s1)
            j=len(s2)
            dp =[0]*(j+1)
            for a in range(1,i+1):
                prev = 0
                for b in range(1,j+1):
                    temp=dp[b]
                    if s1[a-1]==s2[b-1]:
                        dp[b]=1+prev
                    else:
                        dp[b]=max(dp[b-1],dp[b])
                    prev=temp
            return dp[j]
        return LongestCommonSubsequence(text1,text2)