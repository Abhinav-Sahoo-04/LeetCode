class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count=1
        best=1
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                count+=1
                best=max(best,count)
            elif nums[i-1]==nums[i]:
                pass
            else:
                count=1
        return best
        