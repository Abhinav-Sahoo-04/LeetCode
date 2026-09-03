class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # res=[]
        # score=len(nums)//3
        # nums.sort()
        # count=0
        # prev=nums[0]
        # for i in nums:
        #     if prev==i:
        #         count+=1
        #     else:
        #         if count>score:
        #             res.append(prev)
        #         count=1
        #         prev=i
        # if count>score:
        #     res.append(prev)
        # return res

        score=len(nums)//3
        count1=0
        count2=0
        ele1=None
        ele2=None
        for i in nums:
            if ele1==i:
                count1+=1
            elif ele2==i:
                count2+=1
            elif count1==0:
                ele1=i
                count1=1
            elif count2==0:
                ele2=i
                count2=1
            else:
                count1-=1
                count2-=1
        count1 = 0
        count2 = 0

        for i in nums:
            if i == ele1:
                count1 += 1
            elif i == ele2:
                count2 += 1
        res=[]
        if count1>score:
            res.append(ele1)
        if count2>score:
            res.append(ele2)
        return res



        