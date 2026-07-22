class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=float("-inf")
        total=0
        for i in nums:
            total+=i
            maximum=max(maximum,total)
            if total<0:
                total=0
        return maximum