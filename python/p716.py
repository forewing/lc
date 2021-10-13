import heapq


class MaxStack:

    def __init__(self):
        self.q = []
        self.maxi = -1

    def push(self, x: int) -> None:
        self.q.append(x)
        if self.maxi == -1:
            self.maxi = 0
        else:
            if self.q[self.maxi] <= x:
                self.maxi = len(self.q) - 1

    def pop(self) -> int:
        x = self.q[-1]
        self.q.pop()

        if len(self.q) == self.maxi:
            self._find_maxi()

        return x

    def top(self) -> int:
        return self.q[-1]

    def peekMax(self) -> int:
        return self.q[self.maxi]

    def popMax(self) -> int:
        x = self.q[self.maxi]
        self.q.pop(self.maxi)
        self._find_maxi()
        return x

    def _find_maxi(self):
        self.maxi = 0
        for i in range(len(self.q)):
            if self.q[i] >= self.q[self.maxi]:
                self.maxi = i
        if not self.q:
            self.maxi = -1
