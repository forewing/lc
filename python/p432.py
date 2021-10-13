from collections import defaultdict


class AllOne:
    def __init__(self):
        self.key2num = defaultdict(int)
        self.num2key = defaultdict(set)

    def inc(self, key: str) -> None:
        cur = self.key2num[key]
        self.key2num[key] += 1
        self.num2key[cur + 1].add(key)

        if cur != 0:
            self.num2key[cur].remove(key)
            if not self.num2key[cur]:
                self.num2key.pop(cur)

    def dec(self, key: str) -> None:
        cur = self.key2num[key]
        self.num2key[cur].remove(key)
        if not self.num2key[cur]:
            self.num2key.pop(cur)

        if cur == 1:
            self.key2num.pop(key)
        else:
            self.key2num[key] -= 1
            self.num2key[cur - 1].add(key)

    def getMaxKey(self) -> str:
        if not self.num2key:
            return ""

        maxn = max(self.num2key.keys())
        for e in self.num2key[maxn]:
            return e

    def getMinKey(self) -> str:
        if not self.num2key:
            return ""

        minn = min(self.num2key.keys())
        for e in self.num2key[minn]:
            return e
