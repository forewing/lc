class MinStack:

    def __init__(self):
        self.s = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if val <= self.min:
            self.s.append(self.min)
            self.min = val
        self.s.append(val)

    def pop(self) -> None:
        if self.s[-1] == self.min:
            self.s.pop()
            self.min = self.s[-1]
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min
