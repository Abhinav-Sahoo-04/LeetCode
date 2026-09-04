class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        sub=set(nums)
        mini=min(nums)
        maxi=max(nums)
        ans=[]
        for i in range(mini+1,maxi):
            if i not in sub:
                ans.append(i)
        return ans


        