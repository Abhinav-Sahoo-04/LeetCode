class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)//2
            missing=arr[mid]-(mid+1)
            if k>missing:
                low=mid+1
            else:
                high=mid-1
        return high+1+k
            