
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        count=[1]*len(nums)
        maxi=1
        for a in range(1,len(nums)):
            for b in range(a):
                if nums[a]>nums[b] and dp[a]<dp[b]+1:
                    dp[a]=dp[b]+1
                    maxi=max(maxi,dp[a])
                    count[a]=count[b]
                elif nums[a]>nums[b] and dp[b]+1==dp[a]:
                    count[a]+=count[b]
        ans=0
        for a in range(len(dp)):
            if dp[a]==maxi:
                ans+=count[a]
        return ans

        
