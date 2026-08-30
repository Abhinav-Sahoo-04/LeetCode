class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        best=-1
        mini=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>mini:
                best=max(nums[i]-mini,best)
            else:
                mini=nums[i]
        return best