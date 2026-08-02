class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        def SubSumEqualTarget(index,target):
            dp=[False]*(target+1)
            prev=dp[:]
            dp[0]=True
            prev[0]=True
            if nums[0]<=target:
                prev[nums[0]]=True
            for i in range(1,index+1):
                dp = [False] * (target + 1)
                dp[0]=True
                for j in range(1,target+1):
                    notTake=prev[j]
                    take=False
                    if nums[i]<=j:
                        take=prev[j-nums[i]]
                    dp[j]=(take or notTake)
                prev=dp[:]
            return dp[target]
        m=len(nums)
        target=sum(nums)//2
        return SubSumEqualTarget(m-1,target)