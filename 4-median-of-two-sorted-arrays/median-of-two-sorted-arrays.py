class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        # n = len(arr1) + len(arr2)
        # ele1 = -1
        # ele2 = -1
        # ind1 = n // 2
        # ind2 = ind1 - 1
        # i = 0
        # j = 0
        # count = 0
        # while i < len(arr1) and j < len(arr2):
        #     if arr1[i] <= arr2[j]:
        #         if count == ind1:
        #             ele1 = arr1[i]
        #         if count == ind2:
        #             ele2 = arr1[i]
        #         i += 1
        #         count += 1
        #     else:
        #         if count == ind1:
        #             ele1 = arr2[j]
        #         if count == ind2:
        #             ele2 = arr2[j]
        #         j += 1
        #         count += 1
        # while i < len(arr1):
        #     if count == ind1:
        #         ele1 = arr1[i]
        #     if count == ind2:
        #         ele2 = arr1[i]
        #     i += 1
        #     count += 1
        # while j < len(arr2):
        #     if count == ind1:
        #         ele1 = arr2[j]
        #     if count == ind2:
        #         ele2 = arr2[j]
        #     j += 1
        #     count += 1
        # if n % 2 == 1:
        #     return ele1
        # else:
        #     return (ele1 + ele2) / 2
            

        n1=len(arr1)
        n2=len(arr2)
        n=n1+n2
        low=0
        if n1 > n2:
            arr1, arr2 = arr2, arr1
            n1, n2 = n2, n1
        high=n1
        left=(n+1)//2
        while low<=high:
            mid1=(low+high)//2
            mid2=left-mid1
            l1, l2 = float("-inf"), float("-inf")
            r1, r2 = float("inf"), float("inf")
            if mid1<n1:
                r1=arr1[mid1]
            if mid2<n2:
                r2=arr2[mid2]
            if mid1-1>=0 :
                l1=arr1[mid1-1]
            if mid2-1>=0:
                l2=arr2[mid2-1]
            if l1<=r2 and l2<=r1:
                if n%2==1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                high=mid1-1
            else:
                low=mid1+1
                