class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        score=len(nums)//3
        nums.sort()
        count=0
        prev=nums[0]
        for i in nums:
            if prev==i:
                count+=1
            else:
                if count>score:
                    res.append(prev)
                count=1
                prev=i
        if count>score:
            res.append(prev)
        return res



        