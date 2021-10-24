class MyHashMap:

    class Entry:
        def __init__(self, key, val, next):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self):
        self.mod = 100003
        self.list = [self.Entry(-1, -1, None) for _ in range(self.mod)]

    def _index(self, key):
        return key % self.mod

    def _find_pre(self, key):
        index = self._index(key)
        ptr = self.list[index]
        while ptr.next is not None:
            if ptr.next.key == key:
                return ptr
            ptr = ptr.next
        return ptr

    def put(self, key: int, value: int) -> None:
        ptr = self._find_pre(key)
        if ptr.next:
            ptr.next.val = value
        else:
            ptr.next = self.Entry(key, value, None)

    def get(self, key: int) -> int:
        ptr = self._find_pre(key)
        if ptr.next:
            return ptr.next.val
        return -1

    def remove(self, key: int) -> None:
        ptr = self._find_pre(key)
        if ptr.next:
            ptr.next = ptr.next.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


if __name__ == "__main__":
    h = MyHashMap()
    print(h.put(1, 1))
    print(h.put(2, 2))
    print(h.get(1))
    print(h.get(3))
    print(h.remove(2))
    print(h.get(2))
