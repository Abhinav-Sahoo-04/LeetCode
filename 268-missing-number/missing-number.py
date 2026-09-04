class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n=len(nums)+1
        # expected=(n*(n-1))//2
        # real=sum(nums)
        # return expected-real
        xor1=0
        for i in range(len(nums)):
            xor1=xor1^i
            xor1=xor1^nums[i]
        return xor1^(i+1)

        