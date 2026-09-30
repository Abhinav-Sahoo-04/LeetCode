class Solution:
    def maxDepth(self, s: str) -> int:
        best=float("-inf")
        count=0
        stack=[]
        for i in s:
            if i=="(":
                count+=1
                stack.append("(")
                best=max(count,best)
            elif i==")" and stack[-1]=="(":
                count-=1
                stack.pop()
        return max(count,best)
        