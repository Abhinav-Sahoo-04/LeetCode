class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
            def PSE(arr):
                stack=[]
                result=[]
                for b in range(len(arr)):
                    while stack and arr[stack[-1]]>=arr[b]:
                        stack.pop()
                    if not stack:
                        result.append(-1)
                    else:
                        result.append(stack[-1])
                    stack.append(b)
                return result

            def NSE(arr):
                stack=[]
                result=[]
                for a in range(len(arr)-1,-1,-1):
                    while stack and arr[stack[-1]]>=arr[a]:
                        stack.pop()
                    if not stack:
                        result.append(len(arr))
                    else:
                        result.append(stack[-1])
                    stack.append(a)
                return result[::-1]

            def LHA(arr):
                maxi=float("-inf")
                nse=NSE(arr)
                pse=PSE(arr)
                for k in range(len(arr)):
                    area=arr[k]*(nse[k]-pse[k]-1)
                    maxi=max(maxi,area)
                return maxi

            subs=[0]*len(matrix[0])
            res=float("-inf")
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j]=="0":
                        subs[j]=0
                    else:
                        subs[j]=subs[j] + 1
                res=max(res,LHA(subs))
            return res
        