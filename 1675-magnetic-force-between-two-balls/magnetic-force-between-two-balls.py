class Solution:
    def maxDistance(self, arr: list[int], m: int) -> int:
        arr.sort()
        def canPlace(arr,dist,m):
            count=1
            last=arr[0]
            for i in range(1,len(arr)):
                if arr[i]-last>=dist:
                    count+=1
                    last=arr[i]
                if count==m:
                    return True
            return False if count!=m else True
        low,high=1,max(arr)-min(arr)
        best=-1
        while low<=high:
            mid=(low+high)//2
            if canPlace(arr,mid,m):
                best=mid
                low=mid+1
            else:
                high=mid-1
        return best
        