class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = -1

        if not self.mini:
            min_val = val
        
        else:
            min_val = min(self.mini[-1], self.stack[-1])

        self.mini.append(min_val)

    def pop(self) -> None:
        self.mini.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
