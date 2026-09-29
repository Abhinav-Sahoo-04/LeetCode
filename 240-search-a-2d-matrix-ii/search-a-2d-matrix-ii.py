class Solution:
    def searchMatrix(self, arr: List[List[int]], ele: int) -> bool:
        # def bs(arr,ele):
        #     low,high=0,len(arr)-1
        #     while low<=high:
        #         mid=(low+high)//2
        #         if arr[mid]==ele:
        #             return mid
        #         elif arr[mid]>ele:
        #             high=mid-1
        #         else:
        #             low=mid+1
        #     return -1
        # row=-1
        # col=-1
        # for i in range(len(arr)):
        #     row=i
        #     col=bs(arr[i],ele)
        #     if col!=-1:
        #         return True
        # return False

        row=0
        col=len(arr[0])-1
        while row<len(arr) and col>=0:
            if arr[row][col]==ele:
                return True
            elif arr[row][col]>ele:
                col-=1
            else:
                row+=1
        return False
            