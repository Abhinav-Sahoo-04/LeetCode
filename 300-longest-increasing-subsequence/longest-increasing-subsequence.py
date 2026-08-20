class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        i=len(nums)
        dp=[0]*(i+1)
        prev=dp[:]
        for a in range(i-1,-1,-1):
            for b in range(a-1,-2,-1):
                not_take=prev[b+1]
                take=0
                if b==-1 or nums[a]>nums[b]:
                    take=1+prev[a+1]
                dp[b+1]=max(take,not_take)
            prev=dp[:]
        return dp[0]