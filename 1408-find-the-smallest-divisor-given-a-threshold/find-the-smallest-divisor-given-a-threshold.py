class Solution:
    def smallestDivisor(self, arr: List[int], k: int) -> int:
        res=-1
        low=1
        high=max(arr)
        while low<=high:
            mid=(low+high)//2
            total=0
            for j in range(len(arr)):
                total+=math.ceil(arr[j]/mid)
            if total<=k:
                high=mid-1
                res=mid
            else:
                low=mid+1
        return res