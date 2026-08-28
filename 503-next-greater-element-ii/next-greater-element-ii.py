class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        on=len(nums)
        nums=nums+nums
        n=len(nums)
        stack=[]
        result=[]
        i=n-1
        while i >= 0:
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            stack.append(nums[i])
            i-=1
        return result[::-1][:on]
            
