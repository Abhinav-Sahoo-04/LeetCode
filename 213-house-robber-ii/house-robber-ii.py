class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def f(arr):
            prev=arr[0]
            prev2=0
            for i in range(1,len(arr)):
                take=arr[i]
                if i>1:
                    take+=prev2
                notTake=prev
                curr=max(take,notTake)
                prev2=prev
                prev=curr
            return prev

        return max(f(nums[1:]),f(nums[:len(nums)-1]))
        