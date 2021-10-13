class Solution:
    def traverse(self, l, dep):
        for e in l:
            if e.isInteger():
                v = e.getInteger()
                self.sumdep += dep * v
            else:
                self.traverse(e.getList(), dep + 1)

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.sumdep = 0
        self.traverse(nestedList, 1)
        return self.sumdep
