class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        best=float("-inf")
        prefix=1
        suffix=1
        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix*=nums[i]
            suffix*=nums[n-i-1]
            best=max(best,prefix,suffix)
        return best
        