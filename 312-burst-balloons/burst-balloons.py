class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        for i in range(n-2,0,-1):
            for j in range(i,n-1):
                maxi=float("-inf")
                for k in range(i,j+1):
                    cost=(nums[i-1]*nums[k]*nums[j+1])+dp[i][k-1]+dp[k+1][j]
                    maxi=max(cost,maxi)
                dp[i][j]=maxi
        return dp[1][n-2]