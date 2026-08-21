import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # i=len(nums)
        # dp=[1]*i
        # for a in range(i):
        #     for b in range(a):
        #         if nums[a]>nums[b]:
        #             dp[a]=max(dp[b]+1,dp[a])
        # return max(dp)

        temp=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                index=bisect.bisect_left(temp,nums[i])
                print(index)
                len(temp)
                if index==len(temp):
                    temp.append(nums[i])
                else:
                    temp[index]=nums[i]
        return len(temp)
        