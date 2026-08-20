class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        i=len(nums)
        dp=[1]*i
        for a in range(i):
            for b in range(a):
                if nums[a]>nums[b]:
                    dp[a]=max(dp[b]+1,dp[a])
        return max(dp)
        