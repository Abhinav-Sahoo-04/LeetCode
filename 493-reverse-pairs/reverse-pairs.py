class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr=nums
        def MergeSort(low,high):
            def merge(low,mid,high):
                i=low
                j=mid+1
                temp=[]
                while i<=mid and j<=high:
                    if arr[i]<=arr[j]:
                        temp.append(arr[i])
                        i+=1
                    else:
                        temp.append(arr[j])
                        j+=1
                while i<=mid:
                    temp.append(arr[i])
                    i+=1
                while j<=high:
                    temp.append(arr[j])
                    j+=1
                for k in range(low,high+1):
                    arr[k]=temp[k-low]


            if low>=high:
                return 0
            count=0
            mid=(low+high)//2
            count+=MergeSort(low,mid)
            count+=MergeSort(mid+1,high)
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and arr[i] > 2 * arr[j]:
                    j += 1
                count += j - (mid + 1)
            merge(low,mid,high)
            return count
        return MergeSort(0,len(arr)-1)
