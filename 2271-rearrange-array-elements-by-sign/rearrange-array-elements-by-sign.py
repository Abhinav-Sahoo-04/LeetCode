class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        i=0
        j=1
        k=0
        while k<len(nums):
            if nums[k]>=0:
                res[i]=nums[k]
                i+=2
            else:
                res[j]=nums[k]
                j+=2
            k+=1
        return res