class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        def flat(arr):
            res=[]
            for i in arr:
                res+=i
            return res

        arr=flat(grid)
        print(arr)
        s1=0
        sn1=0
        s2=0
        sn2=0
        for i in range(1,len(arr)+1):
            sn1+=i
            sn2+=i**2
        for j in range(len(arr)):
            s1+=arr[j]
            s2+=arr[j]**2
        a=s1-sn1
        b=s2-sn2
        z=b//a
        repeating = (a + z) // 2
        missing = z - repeating
        return [repeating,missing]
            