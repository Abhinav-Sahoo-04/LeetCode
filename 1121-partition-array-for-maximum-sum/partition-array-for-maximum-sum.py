class Solution:
    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            maxi=float("-inf")
            max_ans=float("-inf")
            length=0
            for j in range(i,min(n,i+k)):
                length+=1
                maxi=max(nums[j],maxi)
                cost=length*maxi + dp[j+1]
                max_ans=max(max_ans,cost)
            dp[i]=max_ans
        return dp[0]
        