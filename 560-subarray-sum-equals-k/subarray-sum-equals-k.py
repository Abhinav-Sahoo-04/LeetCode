class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        tab={0:1}
        presum=0
        for i in nums:
            presum+=i
            key=presum-k
            count+=tab.get(key,0)
            tab[presum]=tab.get(presum,0)+1
        return count



        