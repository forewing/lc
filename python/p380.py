import random


class RandomizedSet:

    def __init__(self):
        self.key2ind = {}
        self.keys = []

    def insert(self, val: int) -> bool:
        if val in self.key2ind:
            return False
        self.key2ind[val] = len(self.keys)
        self.keys.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.key2ind:
            return False

        ind = self.key2ind[val]
        last = self.keys[-1]

        self.key2ind[last] = ind
        self.keys[ind] = last

        self.keys.pop()
        del self.key2ind[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.keys)
