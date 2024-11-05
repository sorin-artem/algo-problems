class MinStack:
    stack = []
    min_stack = []

    def __repr__(self):
        return str(self.stack) + " " + str(self.min_stack)

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val)
            min = self.min_stack[-1]
            if val < min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(min)
        else:
            self.stack.append(val)
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(-1)
minStack.push(3)
minStack.push(-4)
print("stack = ", minStack)
print(minStack.getMin())
print(minStack.pop())
print("stack = ", minStack)
print(minStack.getMin())
print(minStack.top())
