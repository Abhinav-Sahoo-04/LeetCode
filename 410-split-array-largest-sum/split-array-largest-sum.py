class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def maxSum(arr,takes,k):
            count=1
            total=0
            best=float("-inf")
            for i in arr:
                if total+i<=takes:
                    total+=i
                else:
                    count+=1
                    total=i
            return count<=k
        low,high=max(nums),sum(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if maxSum(nums,mid,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        
        