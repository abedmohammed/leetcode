class MyQueue(object):
    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def push(self, x):
        self.pushStack.append(x)

    def pop(self):
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack.pop()

    def peek(self):
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack[-1]

    def empty(self):
        return max(len(self.popStack), len(self.pushStack)) == 0


queue = MyQueue()
print(queue.empty())
print(queue.push(1))
print(queue.push(2))
print(queue.push(3))
print(queue.pop())
print(queue.push(4))
print(queue.peek())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.empty())
