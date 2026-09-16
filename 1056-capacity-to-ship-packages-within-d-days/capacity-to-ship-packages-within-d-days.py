class Solution:
    def shipWithinDays(self, arr: list[int], k: int) -> int:
        #Optimal  Solution (Binary Search)
        low,high=max(arr),sum(arr)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            total=0
            count=0
            for j in range(len(arr)):
                total+=arr[j]
                if total>mid:
                    count+=1
                    total=arr[j]
                elif mid==total:
                    count+=1
                    total=0
            if total!=0:
                count+=1
            if count<=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans