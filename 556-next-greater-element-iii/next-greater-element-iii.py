class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums=list(map(int,list(str(n))))
        pivot=len(nums)-2
        while pivot>=0 and nums[pivot]>=nums[pivot+1]:
            pivot-=1
        if pivot==-1:
            return -1
        mini=len(nums)-1
        while mini>pivot and nums[mini]<=nums[pivot]:
            mini-=1
        nums[mini],nums[pivot]=nums[pivot],nums[mini]
        nums[pivot+1:]=reversed(nums[pivot+1:])
        ans= int("".join(map(str,nums)))
        if ans > 2**31 - 1:
            return -1
        return ans
        
       