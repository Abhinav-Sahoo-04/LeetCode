class Solution:
    def searchMatrix(self, arr: list[list[int]], ele: int) -> bool:
        n=len(arr)
        m=len(arr[0])
        low=0
        high=n*m-1
        while low<=high:
            mid=(low+high)//2
            row=mid//m
            col=mid%m
            if arr[row][col]==ele:
                return True
            elif arr[row][col]>ele:
                high=mid-1
            else:
                low=mid+1
        return False