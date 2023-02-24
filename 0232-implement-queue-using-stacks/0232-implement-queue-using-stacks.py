class MyQueue:

    def __init__(self):
        self.queue=[]
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.queue=self.stack[::-1]
      
        

    def pop(self) -> int:
        if self.queue:
            val= self.queue.pop()
            self.stack = self.queue[::-1]
            return val
            
        

    def peek(self) -> int:
        
        return self.stack[0]
        

    def empty(self) -> bool:
        if self.queue:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()