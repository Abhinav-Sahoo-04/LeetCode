class Solution:
    def findPeakGrid(self, arr: list[list[int]]) -> list[int]:
        def maxEle(arr,j,n):
            ele=float("-inf")
            row=-1
            for i in range(n):
                if ele<arr[i][j]:
                    ele=arr[i][j]
                    row=i
            return row


        n=len(arr)
        m=len(arr[0])
        low,high=0,m-1
        while low<=high:
            mid=(low+high)//2
            row=maxEle(arr,mid,n)
            left=arr[row][mid-1] if mid-1>=0 else float("-inf")
            right=arr[row][mid+1] if mid+1<m else float("-inf")
            if arr[row][mid]>left and arr[row][mid]>right:
                return [row,mid]
            elif arr[row][mid]<left:
                high=mid-1
            else:
                low=mid+1