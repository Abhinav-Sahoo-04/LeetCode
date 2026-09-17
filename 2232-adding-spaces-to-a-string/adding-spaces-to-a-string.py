class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i=0
        j=0
        res=""
        while i<len(s) and j<len(spaces):
            if i==spaces[j]:
                res+=" "
                j+=1
            else:
                res+=s[i]
                i+=1
        while i<len(s):
            res+=s[i]
            i+=1
        return res
        