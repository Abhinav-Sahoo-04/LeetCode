class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[-1]*len(arr)
        mini=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            res[i]=mini
            mini=max(arr[i],mini)
        return res
        