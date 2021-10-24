class NestedIterator:
    def __init__(self, nestedList):
        self.l = []
        self.i = 0

        def search(l):
            for e in l:
                if e.isInteger():
                    self.l.append(e.getInteger())
                else:
                    search(e.getList())

        search(nestedList)

    def next(self) -> int:
        ret = self.l[self.i]
        self.i += 1
        return ret

    def hasNext(self) -> bool:
        return self.i < len(self.l)
