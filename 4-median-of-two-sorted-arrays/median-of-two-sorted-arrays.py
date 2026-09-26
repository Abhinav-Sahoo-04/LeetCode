class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        n = len(arr1) + len(arr2)
        ele1 = -1
        ele2 = -1
        ind1 = n // 2
        ind2 = ind1 - 1
        i = 0
        j = 0
        count = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                if count == ind1:
                    ele1 = arr1[i]
                if count == ind2:
                    ele2 = arr1[i]
                i += 1
                count += 1
            else:
                if count == ind1:
                    ele1 = arr2[j]
                if count == ind2:
                    ele2 = arr2[j]
                j += 1
                count += 1
        while i < len(arr1):
            if count == ind1:
                ele1 = arr1[i]
            if count == ind2:
                ele2 = arr1[i]
            i += 1
            count += 1
        while j < len(arr2):
            if count == ind1:
                ele1 = arr2[j]
            if count == ind2:
                ele2 = arr2[j]
            j += 1
            count += 1
        if n % 2 == 1:
            return ele1
        else:
            return (ele1 + ele2) / 2
            
            