class MinStack:

    def __init__(self):
        self.stack =[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minimum = float('inf')
        temp = []
        while len(self.stack) > 0:
            val = self.stack.pop()
            minimum = min(val, minimum)
            temp.append(val)

        while len(temp)>0:
            self.stack.append(temp.pop())
        return minimum
