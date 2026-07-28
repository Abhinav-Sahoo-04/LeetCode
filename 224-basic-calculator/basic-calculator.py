class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        result=0
        num=0
        sign=1
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=="+":
                result+=sign*num
                num=0
                sign=1
            elif i=="-":
                result+=sign*num
                num=0
                sign=-1
            elif i=="(":
                stack.append(result)
                stack.append(sign)
                result=0
                sign=1
            elif i==")":
                result+=sign*num
                num=0
                result*=stack.pop()
                result+=stack.pop()
        result+=sign*num
        return result

