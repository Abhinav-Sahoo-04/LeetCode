class MyStack:

    def __init__(self):
        self.stack=[]
        self.t=-1
        
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.t+=1

        

    def pop(self) -> int:
        if self.t==-1:
            return "Underflow"
        val=self.stack.pop()
        self.t-=1
        return val
        

    def top(self) -> int:
        return self.stack[self.t]
        

    def empty(self) -> bool:
        return False if  self.stack else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()