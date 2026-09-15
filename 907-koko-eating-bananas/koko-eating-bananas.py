class Solution:
    def minEatingSpeed(self, arr: List[int], h: int) -> int:
        high=max(arr)
        low=0
        ans=high
        while low<=high:
            mid=(low+high)//2
            if mid==0:
                break
            hours=0
            for i in arr:
                hours+=(i+mid-1)//mid
            if hours<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans