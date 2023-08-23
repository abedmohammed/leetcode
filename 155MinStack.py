class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mdq = []
        

    def push(self, val):
        self.stack.append(val)
        if not self.mdq or val <= self.mdq[-1]:
            self.mdq.append(val)
        

    def pop(self):
        val = self.stack.pop()
        if val == self.mdq[-1]:
            self.mdq.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.mdq[-1]
        
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(-1)
obj.push(-6)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
