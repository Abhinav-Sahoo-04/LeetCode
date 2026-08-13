class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k=k%sum(chalk)
        i=0
        length=len(chalk)
        while k>0:
            if k<chalk[i]:
                break
            k-=chalk[i]
            i=(i+1)%length
            
        return i
