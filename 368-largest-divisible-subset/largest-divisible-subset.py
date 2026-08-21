class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=len(nums)
        dp=[1]*i
        parent=[-1]*i
        for a in range(1,i):
            for b in range(a):
                if nums[a]%nums[b]==0 and dp[a]<dp[b]+1:
                    dp[a]=dp[b]+1
                    parent[a]=b
        last=0
        for a in range(len(dp)):
            if dp[last] < dp[a]:
                last=a
        ans=[]
        while last!=-1:
            ans.append(nums[last])
            last=parent[last]
        return ans[::-1]

            