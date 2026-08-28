class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack1=[]
        stack2=[]
        pse=[]
        nse=[]
        for i,j in zip(range(len(heights)),range(len(heights)-1,-1,-1)):
            while stack1 and heights[stack1[-1]]>=heights[i]:
                stack1.pop()
            if len(stack1)==0:
                pse.append(-1)
            else:
                pse.append(stack1[-1])
            while stack2 and heights[stack2[-1]]>=heights[j]:
                stack2.pop()
            if len(stack2)==0:
                nse.append(len(heights))
            else:
                nse.append(stack2[-1])
            stack1.append(i)
            stack2.append(j)

        nse=nse[::-1]
        maxi=float("-inf")
        for k in range(len(heights)):
            maxi=max(maxi,heights[k]*(nse[k]-pse[k]-1))
        return maxi