class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def TargetSum(arr,target):
            m=len(arr)-1
            prev=[0]*(target+1)
            if  arr[0]==0:
                prev[0]=2
            else:
                prev[0]=1
            if arr[0]!=0 and arr[0]<=target:
                prev[arr[0]]=1
            for i in range(1,m+1):
                dp=[0]*(target+1)
                dp[0]=prev[0]
                for j in range(target+1):
                    notTake=prev[j]
                    take=0
                    if arr[i]<=j:
                        take=prev[j-arr[i]]
                    dp[j]=take+notTake
                prev=dp[:]
            return prev[target]
        if sum(nums)-target<0 or (sum(nums)-target)%2:
            return 0
        k=(sum(nums)-target)//2
        return TargetSum(nums,k)
        