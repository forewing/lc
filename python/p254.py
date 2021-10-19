class Solution:
    def search(self, target, record, start):
        if record:
            self.ans.append(record + [target])
        for i in range(start, int(target ** 0.5) + 1):
            if target % i == 0:
                self.search(target // i, record + [i], i)

    def getFactors(self, n: int) -> List[List[int]]:
        self.ans = []
        self.search(n, [], 2)
        return self.ans
