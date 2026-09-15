class Solution:
    def minDays(self, arr: List[int], m: int, k: int) -> int:
        if m*k>len(arr):
            return -1
        low=min(arr)
        high=max(arr)
        while low<=high:
            mid=(low+high)//2
            ans=0
            count=0
            for i in range(len(arr)):
                if mid>=arr[i]:
                    count+=1
                else:
                    ans+=count//k
                    count=0
            ans+=count//k
            if ans>=m:
                high=mid-1
            else:
                low=mid+1

        return  low